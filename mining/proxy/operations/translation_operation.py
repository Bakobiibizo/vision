from typing import Tuple, TypeVar

import bittensor as bt

from mining.proxy import core_miner
from mining.proxy.operations import abstract_operation
from models import base_models, synapses
from operation_logic import translation_logic

operation_name = "TranslationOperation"

T = TypeVar("T", bound=bt.Synapse)


class TranslationOperation(abstract_operation.Operation):
    @staticmethod
    @abstract_operation.enforce_concurrency_limits
    async def forward(synapse: synapses.Translation) -> synapses.Translation:
        output = await translation_logic.translation_logic(base_models.TranslationIncoming(**synapse.dict()))
        output_dict = output.dict()
        for field in output_dict:
            setattr(synapse, field, output_dict[field])

        return synapse

    @staticmethod
    def blacklist(synapse: synapses.Translation) -> Tuple[bool, str]:
        return core_miner.base_blacklist(synapse)

    @staticmethod
    def priority(synapse: synapses.Translation) -> float:
        return core_miner.base_priority(synapse)
