import os
from typing import Dict, Any, Optional
from core import constants as core_cst
from rich.prompt import Prompt
from mining.db.db_management import miner_db_manager
from dotenv import load_dotenv

load_dotenv()




def device_processing_func(input: str):
    if "cuda" not in input:
        input = "cuda:" + input
    return input


def optional_http_address_processing_func(input: Optional[str]) -> str:
    if input is None:
        return None
    return http_address_processing_func(input)


def http_address_processing_func(input: str) -> str:
    if "http://" not in input and "https://" not in input:
        input = "http://" + input
    if input[-1] != "/":
        input = input + "/"
    return input


def bool_processing_func(input: str) -> bool:
    if input.lower() in ["true", "t", "1", "y", "yes"]:
        return True
    else:
        return False


def int_processing_func(input: str) -> Optional[int]:
    try:
        return int(input)
    except ValueError:
        return None


GLOBAL_PARAMETERS = {
    core_cst.HOTKEY_PARAM: {"default": os.getenv("WALLET_NAME_PARAM"), "message": "Hotkey name: "},
}

MISC_PARAMETERS = {
    core_cst.WALLET_NAME_PARAM: {"default": "bako_vali", "message": "Wallet Name "},
    core_cst.SUBTENSOR_NETWORK_PARAM: {
        "default": "finney",
        "message": "Subtensor Network (finney, test, local)",
    },
    core_cst.SUBTENSOR_CHAINENDPOINT_PARAM: {
        "default": None,
        "message": "Subtensor Chain Endpoint ",
    },
    core_cst.IS_VALIDATOR_PARAM: {
        "default": "y",
        "message": "Is this a Validator hotkey? (y/n) ",
        "process_function": bool_processing_func,
    },
}

VALIDATOR_PARAMETERS = {
    core_cst.API_SERVER_PORT_PARAM: {
        "default": 4267,
        "message": "API server port (if you're running an organic validator, else leave it)",
    },
    core_cst.EXTERNAL_SERVER_ADDRESS_PARAM: {
        "default": core_cst.EXTERNAL_SERVER_ADDRESS_PARAM,
        "message": "External Server Address: ",
        "process_function": http_address_processing_func,
    },
}

MINER_PARAMETERS = {
    core_cst.AXON_PORT_PARAM: {"default": 4269, "message": "Axon Port: "},
    core_cst.AXON_EXTERNAL_IP_PARAM: {"default": "10.0.3.1", "message": "Axon External IP: "},
    core_cst.IMAGE_WORKER_URL_PARAM: {
        "default": "https://art-celium.ngrok.dev/prompt",
        "message": "Image Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.MIXTRAL_TEXT_WORKER_URL_PARAM: {
        "default": "https://text-agentartificial.ngrok.app/v1/chat/completion",
        "message": "Mixtral Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.LLAMA_3_TEXT_WORKER_URL_PARAM: {
        "default": "https://text-agentartificial.ngrok.app/v1/chat/completion",
        "message": "Llama 3 Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.TRANSLATION_WORKER_URL_PARAM: {
        "default": "https://translation-cellium.ngrok.app/translate",
        "message": "Translation Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
}


gpu_assigned_dict = {}
config = {}

DEFAULT_CONCURRENCY_GROUPS = {"1": 10, "2": 10, "3": 10, "4": 1}


def _insert_defaults_for_task_configs(hotkey: str) -> None:
    miner_db_manager.insert_default_task_configs(hotkey)


def handle_parameters(parameters: Dict[str, Any], hotkey: str):
    global config
    for parameter, metadata in parameters.items():
        if parameter == core_cst.HOTKEY_PARAM:
            continue
        while True:
            try:
                user_input = get_input(metadata)
                config[hotkey][parameter] = user_input
                break
            except ValueError:
                print("Invalid input, please try again.")


def get_input(parameter_metadata: Dict[str, Dict[str, Any]]) -> Any:
    message = (
        f"[yellow]{parameter_metadata['message']}[/yellow][white](default: {parameter_metadata['default']})[/white]"
    )

    user_input = Prompt.ask(message)
    if not user_input:
        user_input = parameter_metadata["default"]

    if parameter_metadata.get("process_function", None) is not None:
        processed_input = parameter_metadata["process_function"](user_input)
        return processed_input
    return user_input


def get_config():
    while True:
        hotkey = get_input(GLOBAL_PARAMETERS[core_cst.HOTKEY_PARAM])
        if hotkey == "":
            break

        config[hotkey] = {}

        handle_parameters(MISC_PARAMETERS, hotkey)

        if config[hotkey][core_cst.IS_VALIDATOR_PARAM]:
            handle_parameters(VALIDATOR_PARAMETERS, hotkey)
        else:
            handle_parameters(MINER_PARAMETERS, hotkey)

            print(
                "\nNote: You must now edit your task configuration (Capacities & concurrency settings). Please use ./peer_at_sql_db.sh, or "
                "use `sqlite3 vision_database.db` to finish your configuration"
            )
            _insert_defaults_for_task_configs(hotkey)

        with open(f".{hotkey}.env", "w") as f:
            f.write(f"{core_cst.HOTKEY_PARAM}=" + hotkey + "\n")
            for key, value in config[hotkey].items():
                f.write(f"{key}=")
                if value is not None:
                    f.write(str(value))
                f.write("\n")

        # Check if the user wants to add another hotkey
        add_another = input("Do you want to add another hotkey? (y/n, default n): ")

        if add_another.lower() != "y":
            break
