from models.base_models import (
    AvatarBase,
    AvatarIncoming,
    AvatarOutgoing,
    BaseOutgoing,
    BaseSynapse,
    CapacityBase,
    CapacityIncoming,
    CapacityOutgoing,
    ChatIncoming,
    ChatOutgoing,
    ChatBase,
    ClipEmbeddingsIncoming,
    ClipEmbeddingsBase,
    ClipEmbeddingsOutgoing,
    ImageGenerationBase,
    ImageResponseBase,
    ImageToImageBase,
    ImageToImageIncoming,
    ImageToImageOutgoing,
    InpaintBase,
    InpaintIncoming,
    InpaintOutgoing,
    TextToImageBase,
    TextToImageIncoming,
    TextToImageOutgoing,
    TranslationBase,
    TranslationOutgoing,
    TranslationIncoming,
    UpscaleBase,
    UpscaleIncoming,
    UpscaleOutgoing,
)
from models import synapses
from models import utility_models
from typing import Optional
from enum import Enum
from core import TASK
import bittensor as bt


class SYNAPSE_TASK(Enum):
    CHAT_MIXTRAL = synapses.Chat
    CHAT_LLAMA_3 = synapses.Chat
    PROTEUS_TEXT_TO_IMAGE = synapses.TextToImage
    PLAYGROUND_TEXT_TO_IMAGE = synapses.TextToImage
    DREAMSHAPER_TEXT_TO_IMAGE = synapses.TextToImage
    PROTEUS_IMAGE_TO_IMAGE = synapses.ImageToImage
    PLAYGROUND_IMAGE_TO_IMAGE = synapses.ImageToImage
    DREAMSHAPER_IMAGE_TO_IMAGE = synapses.ImageToImage
    JUGGER_INPAINT = synapses.Inpaint
    CLIP_IMAGE_EMBEDDING = synapses.ClipEmbeddings
    AVATAR = synapses.Avatar
    TRANSLATION = synapses.Translation


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


__all__ = [
    "AvatarBase",
    "AvatarIncoming",
    "AvatarOutgoing",
    "BaseOutgoing",
    "BaseSynapse",
    "CapacityBase",
    "CapacityIncoming",
    "CapacityOutgoing",
    "ChatIncoming",
    "ChatOutgoing",
    "ChatBase",
    "ClipEmbeddingsIncoming",
    "ClipEmbeddingsBase",
    "ClipEmbeddingsOutgoing",
    "ImageGenerationBase",
    "ImageResponseBase",
    "ImageToImageBase",
    "ImageToImageIncoming",
    "ImageToImageOutgoing",
    "InpaintBase",
    "InpaintIncoming",
    "InpaintOutgoing",
    "TextToImageBase",
    "TextToImageIncoming",
    "TextToImageOutgoing",
    "TranslationBase",
    "TranslationOutgoing",
    "TranslationIncoming",
    "UpscaleBase",
    "UpscaleIncoming",
    "UpscaleOutgoing",
]
