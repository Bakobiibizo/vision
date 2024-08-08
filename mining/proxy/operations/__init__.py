from typing import Any, Dict
from core import TASK as Task
from . import capacity_operation  # noqa
from . import chat_operation  # noqa
from . import text_to_image_operation  # noqa
from . import image_to_image_operation  # noqa
from . import upscale_operation  # noqa
from . import inpaint_operation  # noqa
from . import clip_embeddings_operation  # noqa
from . import avatar_operation  # noqa
from . import translation_operation  # noqa

TASKS_TO_MINER_OPERATION_MODULES: Dict[Task, Any] = {
    "chat_mixtral": chat_operation,
    "chat_llama_3": chat_operation,
    "proteus_text_to_image": text_to_image_operation,
    "playground_text_to_image": text_to_image_operation,
    "dreamshaper_text_to_image": text_to_image_operation,
    "proteus_image_to_image": image_to_image_operation,
    "playground_image_to_image": image_to_image_operation,
    "dreamshaper_image_to_image": image_to_image_operation,
    "jugger_inpainting": inpaint_operation,
    "clip_image_embeddings": clip_embeddings_operation,
    "avatar": avatar_operation,
    "translation": translation_operation,
}
