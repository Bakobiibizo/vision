from pydantic import BaseModel
from typing import Optional
from config import constant_obj as CONSTANTS
from dotenv import load_dotenv
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
    hotkey_name: str = os.getenv("HOTKEY_PARAM") or CONSTANTS.HOTKEY_PARAM
    wallet_name: str = os.getenv("WALLET_NAME_PARAM") or CONSTANTS.WALLET_NAME_PARAM
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
    external_server_url: str = (
        os.getenv("EXTERNAL_SERVER_ADDRESS_PARAM")
        or CONSTANTS.EXTERNAL_SERVER_ADDRESS_PARAM
        or "10.0.3.1"
    )
    api_server_port: Optional[int] = (
        os.getenv("API_SERVER_PORT_PARAM") or CONSTANTS.API_SERVER_PORT_PARAM or 4269
    )
    is_validator: bool = os.getenv("IS_VALIDATOR") or CONSTANTS.IS_VALIDATOR or False


config = Config()
