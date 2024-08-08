from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Optional
from config.create_config import CONSTANTS
import os
import bittensor as bt
import argparse


def _get_env_file_from_cli_config() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_file", type=str, default=None)
    args, _ = parser.parse_known_args()
    env_file = args.env_file

    if not env_file:
        parser.error("You didn't specify an env file! Use --env_file to specify it.")

    return env_file


env_file = _get_env_file_from_cli_config()
if not os.path.exists(env_file):
    bt.logging.error(f"Could not find env file: {env_file}")
load_dotenv(env_file, verbose=True)


class Config(BaseModel):
    hotkey_name: str = os.getenv("HOTKEY_PARAM") or CONSTANTS.HOTKEY_PARAM or None
    wallet_name: str = (
        os.getenv("WALLET_NAME_PARAM") or CONSTANTS.WALLET_NAME_PARAM or None
    )
    subtensor_network: str = (
        os.getenv("SUBTENSOR_NETWORK_PARAM")
        or CONSTANTS.SUBTENSOR_NETWORK_PARAM
        or "finney"
    )
    subtensor_chainendpoint: Optional[str] = (
        os.getenv("SUBTENSOR_CHAINENDPOINT_PARAM")
        or CONSTANTS.SUBTENSOR_CHAINENDPOINT_PARAM
        or None
    )
    image_worker_url: Optional[str] = (
        os.getenv("IMAGE_WORKER_URL_PARAM") or CONSTANTS.IMAGE_WORKER_URL_PARAM or None
    )
    mixtral_text_worker_url: Optional[str] = (
        os.getenv("MIXTRAL_TEXT_WORKER_URL_PARAM")
        or CONSTANTS.MIXTRAL_TEXT_WORKER_URL_PARAM
        or None
    )
    llama_3_text_worker_url: Optional[str] = (
        os.getenv("LLAMA_3_TEXT_WORKER_URL_PARAM")
        or CONSTANTS.LLAMA_3_TEXT_WORKER_URL_PARAM
        or None
    )
    translation_worker_url: Optional[str] = (
        os.getenv("TRANSLATION_WORKER_URL_PARAM")
        or CONSTANTS.TRANSLATION_WORKER_URL_PARAM
        or None
    )
    axon_port: str = os.getenv("AXON_PORT_PARAM") or CONSTANTS.AXON_PORT_PARAM or 4269
    axon_external_ip: str = (
        os.getenv("AXON_EXTERNAL_IP_PARAM")
        or CONSTANTS.AXON_EXTERNAL_IP_PARAM
        or "127.0.0.1"
    )
    debug_miner: bool = (
        os.getenv("DEBUG_MINER_PARAM") or CONSTANTS.DEBUG_MINER_PARAM or False
    )


config = Config()
