import os
import sqlite3
from typing import Dict
from mining.db import sql
from core import TASK, TASK_TO_MAX_CAPACITY
from config import constant_obj as cst
from threading import local
from dotenv import load_dotenv

load_dotenv()


DEFUALT_CONCURRENCY_GROUPS = {
    "CHAT_MIXTRAL": 1,
    "CHAT_LLAMA_3": 2,
    "PROTEUS_TEXT_TO_IMAGE": 3,
    "PLAYGROUND_TEXT_TO_IMAGE": 3,
    "DREAMSHAPER_TEXT_TO_IMAGE": 3,
    "PROTEUS_IMAGE_TO_IMAGE": 3,
    "PLAYGROUND_IMAGE_TO_IMAGE": 3,
    "DREAMSHAPER_IMAGE_TO_IMAGE": 3,
    "JUGGER_INPAINT": 3,
    "CLIP_IMAGE_EMBEDDING": 3,  # disabled clip for now
    "AVATAR": 3,
    "TRANSLATION": 2,
}

DEFAULT_CONCURRENCY_GROUP_VALUES = {1: 7, 2: 7, 3: 1}


class DatabaseManager:
    def __init__(self):
        self.local_data = local()

    def get_connection(self):
        if not hasattr(self.local_data, "conn"):
            self.local_data.conn = sqlite3.connect(cst.VISION_DB)
        return self.local_data.conn

    def close(self):
        if hasattr(self.local_data, "conn"):
            self.local_data.conn.close()

    def read_miner_task_config(self, miner_hotkey: str) -> Dict[str, int]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql.select_tasks_and_number_of_results(), (miner_hotkey,))
        rows = cursor.fetchall()
        return rows

    def insert_default_task_configs(self, miner_hotkey: str) -> None:
        conn = self.get_connection()
        cursor = conn.cursor()

        for task in TASK:
            cursor.execute(
                sql.search_task_config(),
                (
                    task.value,
                    miner_hotkey,
                ),
            )
            if not cursor.fetchone():
                max_capacity = TASK_TO_MAX_CAPACITY[str(task.name)].value
                print(max_capacity)
                default_capacity = int(max_capacity) / 2
                print(DEFUALT_CONCURRENCY_GROUPS)
                concurrency_group_id = DEFUALT_CONCURRENCY_GROUPS[task.name]
                print(concurrency_group_id)
                cursor.execute(
                    sql.insert_default_task_configs(),
                    (
                        task.value,
                        default_capacity,
                        concurrency_group_id,
                        miner_hotkey,
                    ),
                )
        for (
            concurrency_group_id,
            concurrency_group_limit,
        ) in DEFAULT_CONCURRENCY_GROUP_VALUES.items():
            cursor.execute(
                sql.search_concurrency_group_config(),
                (concurrency_group_id,),
            )
            if not cursor.fetchone():
                cursor.execute(
                    sql.insert_default_task_concurrency_group_configs(),
                    (concurrency_group_id, concurrency_group_limit),
                )
        conn.commit()

    def load_concurrency_groups(self) -> Dict[str, int]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql.load_concurrency_groups(), ())
        rows = cursor.fetchall()
        return {str(key): value for key, value in dict(rows).items()}

    def load_task_capacities(self, miner_hotkey: str) -> Dict[str, Dict[str, int]]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql.load_task_capacities(), (miner_hotkey,))
        rows = cursor.fetchall()
        results = {}
        for row in rows:
            task, volume, concurrency_group_id = row
            results[TASK] = {
                "volume": volume,
                "concurrency_group_id": concurrency_group_id,
            }
        return results


miner_db_manager = DatabaseManager()

hotkey = os.getenv("HOTKEY_PARAM")

miner_db_manager.insert_default_task_configs(hotkey)
