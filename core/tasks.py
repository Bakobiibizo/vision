"""Would prefer to make this just one dataclass"""

from enum import Enum
from pydantic import BaseModel
from models import synapses, utility_models
from typing import Dict, Optional
import bittensor as bt


class TASK(Enum):
    CHAT_MIXTRAL = "chat-mixtral"
    CHAT_LLAMA_3 = "chat-llama-3"
    PROTEUS_TEXT_TO_IMAGE = "proteus-text-to-image"
    PLAYGROUND_TEXT_TO_IMAGE = "playground-text-to-image"
    DREAMSHAPER_TEXT_TO_IMAGE = "dreamshaper-text-to-image"
    PROTEUS_TEXT_TO_IMAGE = "proteus-image-to-image"
    PLAYGROUND_IMAGE_TO_IMAGE = "playground-image-to-image"
    DREAMSHAPER_IMAGE_TO_IMAGE = "dreamshaper-image-to-image"
    JUGGER_INPAINT = "inpaint"
    CLIP_IMAGE_EMBEDDING = "clip-image-embeddings"
    AVATAR = "avatar"
    TRANSLATION = "translation"


class STREAMING_TASK(Enum):
    TASK.CHAT_MIXTRAL.name = True
    TASK.CHAT_LLAMA_3.name = True
    TASK.PROTEUS_TEXT_TO_IMAGE.name = False
    TASK.PLAYGROUND_TEXT_TO_IMAGE.name = False
    TASK.DREAMSHAPER_TEXT_TO_IMAGE.name = False
    TASK.PROTEUS_TEXT_TO_IMAGE.name = False
    TASK.PLAYGROUND_IMAGE_TO_IMAGE.name = False
    TASK.DREAMSHAPER_IMAGE_TO_IMAGE.name = False
    TASK.JUGGER_INPAINT.name = False
    TASK.CLIP_IMAGE_EMBEDDING.name = False
    TASK.AVATAR.name = False


class SYNAPSE_TASK(Enum):
    TASK.CHAT_MIXTRAL.name = synapses.Chat
    TASK.CHAT_LLAMA_3.name = synapses.Chat
    TASK.PROTEUS_TEXT_TO_IMAGE.name = synapses.TextToImage
    TASK.PLAYGROUND_TEXT_TO_IMAGE.name = synapses.TextToImage
    TASK.DREAMSHAPER_TEXT_TO_IMAGE.name = synapses.TextToImage
    TASK.PROTEUS_TEXT_TO_IMAGE.name = synapses.ImageToImage
    TASK.PLAYGROUND_IMAGE_TO_IMAGE.name = synapses.ImageToImage
    TASK.DREAMSHAPER_IMAGE_TO_IMAGE.name = synapses.ImageToImage
    TASK.JUGGER_INPAINT.name = synapses.Inpaint
    TASK.CLIP_IMAGE_EMBEDDING.name = synapses.ClipEmbeddings
    TASK.AVATAR.name = synapses.Avatar
    TASK.TRANSLATION.name = synapses.Translation


class TASK_TO_MAX_CAPACITY(Enum):
    TASK.CHAT_MIXTRAL.name = 576_000
    TASK.CHAT_LLAMA_3.name = 576_000
    TASK.PROTEUS_TEXT_TO_IMAGE.name = 3_600
    TASK.PLAYGROUND_TEXT_TO_IMAGE.name = 10_000
    TASK.DREAMSHAPER_TEXT_TO_IMAGE.name = 3_000
    TASK.PROTEUS_TEXT_TO_IMAGE.name = 3_600
    TASK.PLAYGROUND_IMAGE_TO_IMAGE.name = 10_000
    TASK.DREAMSHAPER_IMAGE_TO_IMAGE.name = 3_000
    TASK.JUGGER_INPAINT.name = 4_000
    TASK.CLIP_IMAGE_EMBEDDING.name = (0,)  # disabled clip for no
    TASK.AVATAR.name = 1_120
    TASK.TRANSLATION.name = 64_000


def get_task_from_synapse(synapse: bt.Synapse) -> Optional[TASK]:
    if isinstance(synapse, synapses.Chat):
        if synapse.model == utility_models.ChatModels.mixtral.value:
            return TASK.CHAT_MIXTRAL.value
        elif synapse.model == utility_models.ChatModels.llama_3.value:
            return TASK.CHAT_LLAMA_3.value
        else:
            return None
    elif isinstance(synapse, synapses.TextToImage):
        if synapse.engine == utility_models.EngineEnum.PROTEUS.value:
            return TASK.PROTEUS_TEXT_TO_IMAGE.value
        elif synapse.engine == utility_models.EngineEnum.PLAYGROUND.value:
            return TASK.PLAYGROUND_TEXT_TO_IMAGE.value
        elif synapse.engine == utility_models.EngineEnum.DREAMSHAPER.value:
            return TASK.DREAMSHAPER_TEXT_TO_IMAGE.value
        else:
            return None
    elif isinstance(synapse, synapses.ImageToImage):
        if synapse.engine == utility_models.EngineEnum.PROTEUS.value:
            return TASK.PROTEUS_TEXT_TO_IMAGE.value
        elif synapse.engine == utility_models.EngineEnum.PLAYGROUND.value:
            return TASK.PLAYGROUND_IMAGE_TO_IMAGE.value
        elif synapse.engine == utility_models.EngineEnum.DREAMSHAPER.value:
            return TASK.DREAMSHAPER_IMAGE_TO_IMAGE.value
        else:
            return None
    elif isinstance(synapse, synapses.Inpaint):
        return TASK.JUGGER_INPAINT.value
    elif isinstance(synapse, synapses.ClipEmbeddings):
        return TASK.CLIP_IMAGE_EMBEDDING.value
    elif isinstance(synapse, synapses.Avatar):
        return TASK.AVATAR.value
    elif isinstance(synapse, synapses.Translation):
        return TASK.TRANSLATION.value
    else:
        return None


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
        task=TASK.PROTEUS_TEXT_TO_IMAGE.name,
        overhead=0.5,
        mean=0.18,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.DREAMSHAPER_TEXT_TO_IMAGE.name,
        overhead=0.5,
        mean=0.20,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PLAYGROUND_TEXT_TO_IMAGE.name,
        overhead=0.5,
        mean=0.1,
        variance=10,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PROTEUS_TEXT_TO_IMAGE.name,
        overhead=0.5,
        mean=0.20,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.DREAMSHAPER_IMAGE_TO_IMAGE.name,
        overhead=0.5,
        mean=0.27,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.PLAYGROUND_IMAGE_TO_IMAGE.name,
        overhead=0.5,
        mean=0.10,
        variance=10,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.JUGGER_INPAINT.name,
        overhead=1.2,
        mean=0.15,
        variance=2,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.AVATAR.name,
        overhead=5,
        mean=0.40,
        variance=3,
        task_type=TaskType.IMAGE,
    ),
    TaskConfig(
        task=TASK.CHAT_MIXTRAL.name,
        overhead=1,
        mean=0.006,
        variance=80,
        task_type=TaskType.TEXT,
    ),
    TaskConfig(
        task=TASK.CHAT_LLAMA_3.name,
        overhead=1,
        mean=0.008,
        variance=80,
        task_type=TaskType.TEXT,
    ),
    TaskConfig(
        task=TASK.CLIP_IMAGE_EMBEDDING.name,
        overhead=1,
        mean=0.5,
        variance=2,
        task_type=TaskType.CLIP,
    ),
    TaskConfig(
        task=TASK.TRANSLATION.name,
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
    raise ValueError(f"Task configuration for {TASK.value.name} not found")
