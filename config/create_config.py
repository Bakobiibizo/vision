import os
from typing import Dict, Any, Optional, List, Tuple
from rich.prompt import Prompt
from pydantic import BaseModel, Field
from pydantic.root_model import RootModel
from enum import Enum
from dotenv import set_key, load_dotenv


class Constants(BaseModel):
    SCORING_PERIOD_TIME: int
    SEED_CHUNK_SIZE: int
    TASK_CONFIG_JSON: str
    TASK_CONCURRENCY_CONFIG_JSON: str
    BLOCKS_PER_EPOCH: int
    BLOCK_TIME_IN_S: int
    SPECIAL_CONCEPTS: List[str]
    NSFW_CONCEPTS: List[str]
    NSFW_RESPONSE_ERROR: str
    LUNA_DIFFUSION_REPO: str
    DEFAULT_NEGATIVE_PROMPT: str
    KANDINKSY_NEGATIVE_PROMPT_PERFIX: str
    LARGEST_SEED: int
    DEFAULT_CFG_SCALE: int
    DEFAULT_HEIGHT: int
    DEFAULT_WIDTH: int
    DEFAULT_SAMPLES: int
    DEFAULT_STEPS: int
    DEFAULT_STYLE_PRESET: Optional[str]
    DEFAULT_IMAGE_STRENGTH: float
    DEFAULT_INIT_IMAGE_MODE: str
    DEFAULT_SAMPLER: Optional[str]
    DEFAULT_ENGINE: str
    UPSCALE_ENGINE: str
    ALLOWED_IMAGE_SIZES: List[Tuple[int, int]]
    DEBUG_MINER_PARAM: bool
    MODEL_CLIP: str
    AVAILABLE_TASKS_OPERATION: str
    MODEL_SDXL_TURBO: str
    MODEL_SCRIBBLE: str
    MODEL_MARKOV: str
    MODEL_CACHE: str
    MODEL_UPSCALE: str
    PROMPT_SAFETY_CHECKERS: str
    IMAGE_SAFETY_CHECKERS: str
    DEVICE_DEFAULT: str
    CONFIG_FILEPATH: str
    OPERATION_TEXT_TO_IMAGE: str
    OPERATION_IMAGE_TO_IMAGE: str
    OPERATION_INPAINT: str
    OPERATION_UPSCALE: str
    OPERATION_SEGMENT: str
    OPERATION_CLIP_EMBEDDINGS: str
    OPERATION_SCRIBBLE: str
    OPERATION_TRANSLATION: str
    CLIP_MODEL_REPO: str
    DREAMSHAPER_XL_LOCAL_FILE: str
    KANDINSKY_PIPELINE_REPO: str
    INPAINT_PIPELINE_REPO: str
    DREAMSHAPER_PIPELINE_REPO: str
    CONTROL_MODEL_REPO: str
    DATASET_REPO: str
    IS_VALIDATOR: bool
    CACHE_PATH: str
    CACHE_SIZE: int
    CHECKPOINT_PATH: str
    MODEL_TYPE: str
    MODELS_CACHE: str
    PRIOR_STEPS: int
    PRIOR_GUIDANCE_SCALE: float
    SYNTHETIC_ENDPOINT_PREFIX: str
    CHECKING_ENDPOINT_PREFIX: str
    OUTGOING: str
    SINGULAR_GPU: str
    HOTKEY_PARAM: str
    IMAGE_WORKER_URL_PARAM: str
    MIXTRAL_TEXT_WORKER_URL_PARAM: str
    LLAMA_3_TEXT_WORKER_URL_PARAM: str
    TRANSLATION_WORKER_URL_PARAM: str
    SAFETY_CHECKERS_PARAM: str
    CLIP_DEVICE_PARAM: str
    SCRIBBLE_DEVICE_PARAM: str
    KANDINSKY_DEVICE_PARAM: str
    SDXL_TURBO_DEVICE_PARAM: str
    UPSCALE_DEVICE_PARAM: str
    WALLET_NAME_PARAM: str
    SUBTENSOR_NETWORK_PARAM: str
    SUBTENSOR_CHAIN_ENDPOINT_PARAM: str
    IS_VALIDATOR_PARAM: bool
    API_SERVER_PORT_PARAM: int
    EXTERNAL_SERVER_ADDRESS_PARAM: str
    AXON_PORT_PARAM: int
    AXON_EXTERNAL_IP_PARAM: str
    VISION_DB: str
    TASKS_CONFIG_TABLE: str
    TASKS_CONCURRENCY_CONFIG_TABLE: str
    CONCURRENCY_GROUP_LIMIT: str
    TASK_NAME: str
    VOLUME: str
    MINER_HOTKEY: str
    CONCURRENCY_GROUP_ID: str


NSFW_CONCEPTS = [
    "sexual",
    "nude",
    "sex",
    "18+",
    "naked",
    "nsfw",
    "porn",
    "dick",
    "vagina",
    "naked child",
    "explicit content",
    "uncensored",
    "fuck",
    "nipples",
    "visible nipples",
    "naked breasts",
    "areola",
]
constant_obj = Constants(
    SCORING_PERIOD_TIME=60 * 60,
    SEED_CHUNK_SIZE=100_000,
    TASK_CONFIG_JSON="task_config.json",
    TASK_CONCURRENCY_CONFIG_JSON="task_concurrency_config.json",
    BLOCKS_PER_EPOCH=360,
    BLOCK_TIME_IN_S=12,
    SPECIAL_CONCEPTS=[
        "little girl",
        "young child",
        "young girl",
        "little boy",
        "young boy",
    ],
    NSFW_CONCEPTS=NSFW_CONCEPTS,
    NSFW_RESPONSE_ERROR="error_nsfw_image",
    LUNA_DIFFUSION_REPO="proximasanfinetuning/luna-diffusion",
    DEFAULT_NEGATIVE_PROMPT=", ".join(NSFW_CONCEPTS) + ", worst quality, low quality",
    KANDINKSY_NEGATIVE_PROMPT_PERFIX="overexposed",
    LARGEST_SEED=4294967295,
    DEFAULT_CFG_SCALE=7,
    DEFAULT_HEIGHT=1024,
    DEFAULT_WIDTH=1024,
    DEFAULT_SAMPLES=1,
    DEFAULT_STEPS=4,
    DEFAULT_STYLE_PRESET=None,
    DEFAULT_IMAGE_STRENGTH=0.20,
    DEFAULT_INIT_IMAGE_MODE="IMAGE_STRENGTH",
    DEFAULT_SAMPLER=None,
    DEFAULT_ENGINE="dreamshaperxlalpha",
    UPSCALE_ENGINE="esrgan-v1-x2plus",
    ALLOWED_IMAGE_SIZES=[
        (1024, 1024),
        (1152, 896),
        (1216, 832),
        (1344, 768),
        (1536, 640),
        (640, 1536),
        (768, 1344),
        (832, 1216),
        (896, 1152),
    ],
    DEBUG_MINER_PARAM=False,
    MODEL_CLIP="clip",
    AVAILABLE_TASKS_OPERATION="available_tasks_operation",
    MODEL_SDXL_TURBO="sdxl_turbo",
    MODEL_SCRIBBLE="scribble",
    MODEL_MARKOV="markov",
    MODEL_CACHE="cache",
    MODEL_UPSCALE="upscale",
    PROMPT_SAFETY_CHECKERS="prompt_safety_checkers",
    IMAGE_SAFETY_CHECKERS="image_safety_checkers",
    DEVICE_DEFAULT="cuda",
    CONFIG_FILEPATH="config.yaml",
    OPERATION_TEXT_TO_IMAGE="TextToImage",
    OPERATION_IMAGE_TO_IMAGE="ImageToImage",
    OPERATION_INPAINT="Inpaint",
    OPERATION_UPSCALE="Upscale",
    OPERATION_SEGMENT="Segment",
    OPERATION_CLIP_EMBEDDINGS="ClipEmbeddings",
    OPERATION_SCRIBBLE="Scribble",
    OPERATION_TRANSLATION="Translation",
    CLIP_MODEL_REPO="laion/CLIP-ViT-bigG-14-laion2B-39B-b160k",
    DREAMSHAPER_XL_LOCAL_FILE="dreamshaperxlalpha.safetensors",
    KANDINSKY_PIPELINE_REPO="kandinsky-community/kandinsky-2-2-decoder",
    INPAINT_PIPELINE_REPO="kandinsky-community/kandinsky-2-2-decoder-inpaint",
    DREAMSHAPER_PIPELINE_REPO="Lykon/dreamshaper-8",
    CONTROL_MODEL_REPO="xinsir/controlnet-union-sdxl-1.0",
    DATASET_REPO="Bakobiibizo/train14",
    IS_VALIDATOR=True,
    CACHE_PATH="image_cache",
    CACHE_SIZE=40 * 1024**2,
    CHECKPOINT_PATH="models/sam_vit_l_0b3195.pth",
    MODEL_TYPE="vit_l",
    MODELS_CACHE="models_cache",
    PRIOR_STEPS=25,
    PRIOR_GUIDANCE_SCALE=1.0,
    SYNTHETIC_ENDPOINT_PREFIX="synthetic",
    CHECKING_ENDPOINT_PREFIX="checking",
    OUTGOING="Outgoing",
    SINGULAR_GPU="",
    HOTKEY_PARAM="bako_hot",
    IMAGE_WORKER_URL_PARAM="http://100.64.221.101:8188/prompt",
    MIXTRAL_TEXT_WORKER_URL_PARAM="http://100.117.156.73:7099/v1/chat/completions",
    LLAMA_3_TEXT_WORKER_URL_PARAM="http:100.117.156.73/v1/chat/completions",
    TRANSLATION_WORKER_URL_PARAM="http://100.77.94.60:4269/translate",
    SAFETY_CHECKERS_PARAM="cuda:0",
    CLIP_DEVICE_PARAM="cuda:1",
    SCRIBBLE_DEVICE_PARAM="cuda:2",
    KANDINSKY_DEVICE_PARAM="cuda:3",
    SDXL_TURBO_DEVICE_PARAM="cuda:4",
    UPSCALE_DEVICE_PARAM="cuda:5",
    WALLET_NAME_PARAM="bako_vali",
    SUBTENSOR_NETWORK_PARAM="finney",
    SUBTENSOR_CHAIN_ENDPOINT_PARAM="entrypoint-finney.opentensor.ai",
    IS_VALIDATOR_PARAM=True,
    API_SERVER_PORT_PARAM=4267,
    EXTERNAL_SERVER_ADDRESS_PARAM="0.0.0.0",
    AXON_PORT_PARAM=4269,
    AXON_EXTERNAL_IP_PARAM="0.0.0.0",
    VISION_DB="vision_database.db",
    TASKS_CONFIG_TABLE="miner_task_config",
    TASKS_CONCURRENCY_CONFIG_TABLE="miner_concurrency_group",
    CONCURRENCY_GROUP_LIMIT="concurrent_tasks_limit",
    TASK_NAME="task_name",
    VOLUME="volume",
    MINER_HOTKEY="miner_hotkey",
    CONCURRENCY_GROUP_ID="concurrency_group_id",
)


for key, value in constant_obj.model_dump().items():
    set_key("./.env", key, str(value))

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
    constant_obj.HOTKEY_PARAM: {
        "default": constant_obj.HOTKEY_PARAM,
        "message": "Hotkey name: ",
    },
}

MISC_PARAMETERS = {
    constant_obj.WALLET_NAME_PARAM: {
        "default": constant_obj.WALLET_NAME_PARAM,
        "message": "Wallet Name ",
    },
    constant_obj.SUBTENSOR_NETWORK_PARAM: {
        "default": constant_obj.SUBTENSOR_NETWORK_PARAM,
        "message": "Subtensor Network (finney, test, local)",
    },
    constant_obj.SUBTENSOR_CHAIN_ENDPOINT_PARAM: {
        "default": constant_obj.SUBTENSOR_CHAIN_ENDPOINT_PARAM,
        "message": "Subtensor Chain Endpoint ",
    },
    constant_obj.IS_VALIDATOR_PARAM: {
        "default": constant_obj.IS_VALIDATOR_PARAM,
        "message": "Is this a Validator hotkey? (y/n) ",
        "process_function": bool_processing_func,
    },
}

VALIDATOR_PARAMETERS = {
    constant_obj.API_SERVER_PORT_PARAM: {
        "default": constant_obj.API_SERVER_PORT_PARAM,
        "message": "API server port (if you're running an organic validator, else leave it)",
    },
    constant_obj.EXTERNAL_SERVER_ADDRESS_PARAM: {
        "default": constant_obj.EXTERNAL_SERVER_ADDRESS_PARAM,
        "message": "External Server Address: ",
        "process_function": http_address_processing_func,
    },
}

MINER_PARAMETERS = {
    constant_obj.AXON_PORT_PARAM: {
        "default": constant_obj.AXON_PORT_PARAM,
        "message": "Axon Port: ",
    },
    constant_obj.AXON_EXTERNAL_IP_PARAM: {
        "default": constant_obj.AXON_EXTERNAL_IP_PARAM,
        "message": "Axon External IP: ",
    },
    constant_obj.IMAGE_WORKER_URL_PARAM: {
        "default": constant_obj.IMAGE_WORKER_URL_PARAM,
        "message": "Image Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    constant_obj.MIXTRAL_TEXT_WORKER_URL_PARAM: {
        "default": constant_obj.MIXTRAL_TEXT_WORKER_URL_PARAM,
        "message": "Mixtral Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    constant_obj.LLAMA_3_TEXT_WORKER_URL_PARAM: {
        "default": constant_obj.LLAMA_3_TEXT_WORKER_URL_PARAM,
        "message": "Llama 3 Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    constant_obj.TRANSLATION_WORKER_URL_PARAM: {
        "default": constant_obj.TRANSLATION_WORKER_URL_PARAM,
        "message": "Translation Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
}


gpu_assigned_dict = {}
config = {}

DEFAULT_CONCURRENCY_GROUPS = {"1": 10, "2": 10, "3": 10, "4": 1}


def handle_parameters(parameters: Dict[str, Any], hotkey: str):
    global config
    for parameter, metadata in parameters.items():
        if parameter:
            continue
        while True:
            try:
                user_input = get_input(metadata)
                config[hotkey][parameter] = user_input
                break
            except ValueError:
                print("Invalid input, please try again.")


def get_input(parameter_metadata: Dict[str, Dict[str, Any]]) -> Any:
    message = f"[yellow]{parameter_metadata['message']}[/yellow][white](default: {parameter_metadata['default']})[/white]"

    user_input = Prompt.ask(message)
    if not user_input:
        user_input = parameter_metadata["default"]

    if parameter_metadata.get("process_function", None) is not None:
        processed_input = parameter_metadata["process_function"](user_input)
        return processed_input
    return user_input


def get_config():
    while True:
        hotkey = get_input(GLOBAL_PARAMETERS[constant_obj.HOTKEY_PARAM])
        if hotkey == "":
            break

        config[hotkey] = {}

        handle_parameters(MISC_PARAMETERS, hotkey)

        if config[hotkey][constant_obj.IS_VALIDATOR_PARAM]:
            handle_parameters(VALIDATOR_PARAMETERS, hotkey)
        else:
            handle_parameters(MINER_PARAMETERS, hotkey)

            print(
                "\nNote: You must now edit your task configuration (Capacities & concurrency settings). Please use ./peer_at_sql_db.sh, or "
                "use `sqlite3 vision_database.db` to finish your configuration"
            )

        with open(f".{hotkey}.env", "w") as f:
            f.write(f"{constant_obj.HOTKEY_PARAM}=" + hotkey + "\n")
            for key, value in config[hotkey].items():
                f.write(f"{key}=")
                if value is not None:
                    f.write(str(value))
                f.write("\n")

        # Check if the user wants to add another hotkey
        add_another = input("Do you want to add another hotkey? (y/n, default n): ")

        if add_another.lower() != "y":
            break
