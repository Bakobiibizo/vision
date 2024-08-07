import bittensor as bt
from models import base_models
from operation_logic import utils as operation_utils
from modules.translation.translation import Translation
from modules.translation.data_models import TranslationRequest


POST_ENDPOINT = "translation"

translation_module = Translation()

async def translation_logic(
    body: base_models.TranslationIncoming,
) -> base_models.TranslationOutgoing:
    """Add gpu potential"""

    output = base_models.TranslationOutgoing()

    translation_response_body = await operation_utils.get_translation_from_server(body, POST_ENDPOINT, timeout=15)
    # If safe for work but still no translations, something went wrong probably
    if translation_response_body is None or translation_response_body.translation_b64 is None:
        output.error_message = "Some error from the generation :/"
        return output
    else:
        bt.logging.info("✅ Generated an translation ✨")
        output.translation_b64 = translation_response_body.translation_b64
        output.is_nsfw = False

    output.clip_embeddings = translation_response_body.clip_embeddings
    output.translation_hashes = translation_response_body.translation_hashes

    return output


def translation_request(request: TranslationRequest):