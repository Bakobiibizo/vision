from abc import ABC
from typing import Tuple

import bittensor as bt
from segment_anything import SamPredictor, sam_model_registry

from core import constants as cst


class BaseValidator(ABC):
    def __init__(self, dendrite, config, subtensor, wallet, timeout):
        self.dendrite = dendrite
        self.config = config
        self.subtensor = subtensor
        self.wallet = wallet
        self.timeout = timeout
        self.streaming = False
        sam = sam_model_registry[cst.MODEL_TYPE](checkpoint=cst.CHECKPOINT_PATH)
        sam.to(device="cuda")
        self.predictor = SamPredictor(sam)

    async def query_miner(self, axon: bt.axon, uid: int, syn: bt.Synapse) -> Tuple[int, bt.Synapse]:
        bt.logging.info(f"Querying miner with uid {uid} and axon {axon}")
        try:
            responses = await self.dendrite(
                [axon],
                syn,
                deserialize=False,
                timeout=self.timeout,
                streaming=self.streaming,
            )
            return await self.handle_response(uid, responses)

        except Exception as e:
            bt.logging.error(f"Exception during query for uid {uid}: {e}")
            return uid, None

    async def handle_response(self, uid: int, responses: list[bt.Synapse]) -> Tuple[int, bt.Synapse]:
        return uid, responses[0]
