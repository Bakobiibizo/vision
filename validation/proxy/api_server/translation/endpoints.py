from core import Task
import fastapi
from fastapi.responses import JSONResponse
from models import base_models, synapses, utility_models, request_models
from validation.proxy import get_synapse, validation_utils
from fastapi import HTTPException, routing
from validation.proxy.api_server.image import utils
from validation.core_validator import core_validator

from validation.proxy import dependencies

router = routing.APIRouter(tags=["translation"])

@router.post("/translate")
async def translation(
    body: request_models.TranslationRequest,
    _: None = fastapi.Depends(dependencies.get_token),
) -> request_models.TranslationRequest:
    synapse: synapses.Translation = get_synapse.get_synapse_from_body(
        body=body,
        synapse_model=synapses.Translation,
    )

    result: utility_models.QueryResult = await core_validator.make_organic_query(
        synapse=synapse,
        outgoing_model=base_models.TranslationIncoming,
        task=Task(synapse.engine + "-translation"),
        stream=False,
    )
    if isinstance(result, JSONResponse):
        return result
    validation_utils.handle_bad_result(result)

    formatted_response: base_models.TranslationOutgoing = result.formatted_response

    return request_models.TranslationRequest(image_b64=formatted_response.image_b64)