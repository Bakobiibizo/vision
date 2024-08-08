import importlib
import time
import tracemalloc

import bittensor as bt
from core import utils, TASK as Task
from mining.proxy import core_miner
from config import constant_obj as config, miner_config
from mining.proxy import operations

# For determinism

tracemalloc.start()

if __name__ == "__main__":
    miner = core_miner.CoreMiner()

    bt.logging.info("Loading all config & resources....")
    try:
        if config.debug_miner:
            bt.logging.debug("Miner is in debug mode 🪳🔫")
    except Exception as e:
        bt.logging.info("Miner is in debug mode")

    capacity_module = importlib.import_module(
        "mining.proxy.operations.translation_operation"
    )

    CapacityClass = getattr(capacity_module, "TranslationOperation")
    miner.attach_to_axon(
        CapacityClass.forward, CapacityClass.blacklist, CapacityClass.priority
    )

    task_and_capacities = utils.load_capacities(config.HOTKEY_PARAM)
    operations_supported = set()
    if not config.DEBUG_MINER_PARAM:
        for task in Task:
            operation_module = operations.TASKS_TO_MINER_OPERATION_MODULES["translation"]
            if operation_module not in operations_supported:
                operations_supported.add(operation_module)
                operation_class = getattr(operation_module, "TranslationOperation")
                miner.attach_to_axon(
                    getattr(operation_class, "forward"),
                    getattr(operation_class, "blacklist"),
                    getattr(operation_class, "priority"),
                )

    with miner as running_miner:
        while True:
            time.sleep(240)
