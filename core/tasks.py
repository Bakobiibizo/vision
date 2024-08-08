"""Would prefer to make this just one dataclass"""

from enum import Enum
from pydantic import BaseModel
from typing import Dict, Optional
import bittensor as bt


class TASK(Enum):
    CHAT_MIXTRAL = "chat-mixtral"
    CHAT_LLAMA_3 = "chat-llama-3"
    PROTEUS_TEXT_TO_IMAGE = "proteus-text-to-image"
    PLAYGROUND_TEXT_TO_IMAGE = "playground-text-to-image"
    DREAMSHAPER_TEXT_TO_IMAGE = "dreamshaper-text-to-image"
    PROTEUS_IMAGE_TO_IMAGE = "proteus-image-to-image"
    PLAYGROUND_IMAGE_TO_IMAGE = "playground-image-to-image"
    DREAMSHAPER_IMAGE_TO_IMAGE = "dreamshaper-image-to-image"
    JUGGER_INPAINT = "inpaint"
    CLIP_IMAGE_EMBEDDING = "clip-image-embeddings"
    AVATAR = "avatar"
    TRANSLATION = "translation"


class STREAMING_TASK(Enum):
    CHAT_MIXTRAL = True
    CHAT_LLAMA_3 = True
    PROTEUS_TEXT_TO_IMAGE = False
    PLAYGROUND_TEXT_TO_IMAGE = False
    DREAMSHAPER_TEXT_TO_IMAGE = False
    PROTEUS_IMAGE_TO_IMAGE = False
    PLAYGROUND_IMAGE_TO_IMAGE = False
    DREAMSHAPER_IMAGE_TO_IMAGE = False
    JUGGER_INPAINT = False
    CLIP_IMAGE_EMBEDDING = False
    AVATAR = False


class TASK_TO_MAX_CAPACITY(Enum):
    CHAT_MIXTRAL = 576_000
    CHAT_LLAMA_3 = 576_000
    PROTEUS_TEXT_TO_IMAGE = 3_600
    PLAYGROUND_TEXT_TO_IMAGE = 10_000
    DREAMSHAPER_TEXT_TO_IMAGE = 3_000
    PROTEUS_IMAGE_TO_IMAGE = 3_600
    PLAYGROUND_IMAGE_TO_IMAGE = 10_000
    DREAMSHAPER_IMAGE_TO_IMAGE = 3_000
    JUGGER_INPAINT = 4_000
    CLIP_IMAGE_EMBEDDING = 0  # disabled clip for no
    AVATAR = 1_120
    TRANSLATION = 64_000


class TaskType(Enum):
    IMAGE = "image"
    TEXT = "text"
    CLIP = "clip"
    TRANSLATION = "transl"


class TaskConfig(BaseModel):
    task: TASK
    overhead: float
    mean: float
    variance: float
    task_type: TaskType


TASK_CONFIGS = [
    TaskConfig(
        task=TASK.PROTEUS_TEXT_TO_IMAGE,
        overhead=0.5,
        mean=0.18,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.DREAMSHAPER_TEXT_TO_IMAGE,
        overhead=0.5,
        mean=0.20,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PLAYGROUND_TEXT_TO_IMAGE,
        overhead=0.5,
        mean=0.1,
        variance=10,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PROTEUS_IMAGE_TO_IMAGE,
        overhead=0.5,
        mean=0.20,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.DREAMSHAPER_IMAGE_TO_IMAGE,
        overhead=0.5,
        mean=0.27,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PLAYGROUND_IMAGE_TO_IMAGE,
        overhead=0.5,
        mean=0.10,
        variance=10,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.JUGGER_INPAINT,
        overhead=1.2,
        mean=0.15,
        variance=2,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.AVATAR,
        overhead=5,
        mean=0.40,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.CHAT_MIXTRAL,
        overhead=1,
        mean=0.006,
        variance=80,
        task_type=TaskType.TEXT,
    ),
    TaskConfig(
        task=TASK.CHAT_LLAMA_3,
        overhead=1,
        mean=0.008,
        variance=80,
        task_type=TaskType.TEXT,
    ),
    TaskConfig(
        task=TASK.CLIP_IMAGE_EMBEDDING,
        overhead=1,
        mean=0.5,
        variance=2,
        task_type=TaskType.CLIP,
    ),
    TaskConfig(
        task=TASK.TRANSLATION,
        overhead=1,
        mean=0.5,
        variance=1,
        task_type=TaskType.TRANSLATION,
    ),
]


def get_task_config(task: TASK) -> TaskConfig:
    for config in TASK_CONFIGS:
        if config.task == task:
            return config
    raise ValueError(f"Task configuration for {TASK.value} not found")
