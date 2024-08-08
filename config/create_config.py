import os
from typing import Dict, Any, Optional, List, Tuple
from core import constants as core_cst
from rich.prompt import Prompt
from mining.db.db_management import miner_db_manager
from pydantic import BaseModel, Field
from enum import Enum
from dotenv import set_key, load_dotenv


class ConstantsObj(BaseModel):
    __root__: Dict[str, Any] = Field(default_factory=dict)

    def __getitem__(self, key: str) -> Any:
        return self.__root__[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.__root__[key] = value

    @classmethod
    def create(cls, **kwargs):
        return cls(__root__=kwargs)


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
constant_obj = ConstantsObj(
    __root__={
        "SCORING_PERIOD_TIME": 60 * 60,
        "SEED_CHUNK_SIZE": 100_000,
        "TASK_CONFIG_JSON": "task_config.json",
        "TASK_CONCURRENCY_CONFIG_JSON": "task_concurrency_config.json",
        "BLOCKS_PER_EPOCH": 360,
        "BLOCK_TIME_IN_S": 12,
        "SPECIAL_CONCEPTS": [
            "little girl",
            "young child",
            "young girl",
            "little boy",
            "young boy",
        ],
        "NSFW_CONCEPTS": NSFW_CONCEPTS,
        "NSFW_RESPONSE_ERROR": "error_nsfw_image",
        "LUNA_DIFFUSION_REPO": "proximasanfinetuning/luna-diffusion",
        "DEFAULT_NEGATIVE_PROMPT": ", ".join(NSFW_CONCEPTS)
        + ", worst quality, low quality",
        "KANDINKSY_NEGATIVE_PROMPT_PERFIX": "overexposed",
        "LARGEST_SEED": 4294967295,
        "DEFAULT_CFG_SCALE": 7,
        "DEFAULT_HEIGHT": 1024,
        "DEFAULT_WIDTH": 1024,
        "DEFAULT_SAMPLES": 1,
        "DEFAULT_STEPS": 4,
        "DEFAULT_STYLE_PRESET": None,
        "DEFAULT_IMAGE_STRENGTH": 0.20,
        "DEFAULT_INIT_IMAGE_MODE": "IMAGE_STRENGTH",
        "DEFAULT_SAMPLER": None,
        "DEFAULT_ENGINE": "dreamshaperxlalpha",
        "UPSCALE_ENGINE": "esrgan-v1-x2plus",
        "ALLOWED_IMAGE_SIZES": [
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
        "DEBUG_MINER_PARAM": "debug_miner",
        "MODEL_CLIP": "clip",
        "AVAILABLE_TASKS_OPERATION": "available_tasks_operation",
        "MODEL_SDXL_TURBO": "sdxl_turbo",
        "MODEL_SCRIBBLE": "scribble",
        "MODEL_MARKOV": "markov",
        "MODEL_CACHE": "cache",
        "MODEL_UPSCALE": "upscale",
        "PROMPT_SAFETY_CHECKERS": "prompt_safety_checkers",
        "IMAGE_SAFETY_CHECKERS": "image_safety_checkers",
        "DEVICE_DEFAULT": "cuda",
        "CONFIG_FILEPATH": "config.yaml",
        "OPERATION_TEXT_TO_IMAGE": "TextToImage",
        "OPERATION_IMAGE_TO_IMAGE": "ImageToImage",
        "OPERATION_INPAINT": "Inpaint",
        "OPERATION_UPSCALE": "Upscale",
        "OPERATION_SEGMENT": "Segment",
        "OPERATION_CLIP_EMBEDDINGS": "ClipEmbeddings",
        "OPERATION_SCRIBBLE": "Scribble",
        "OPERATION_TRANSLATION": "Translation",
        "CLIP_MODEL_REPO": "laion/CLIP-ViT-bigG-14-laion2B-39B-b160k",
        "DREAMSHAPER_XL_LOCAL_FILE": "dreamshaperxlalpha.safetensors",
        "KANDINSKY_PIPELINE_REPO": "kandinsky-community/kandinsky-2-2-decoder",
        "INPAINT_PIPELINE_REPO": "kandinsky-community/kandinsky-2-2-decoder-inpaint",
        "DREAMSHAPER_PIPELINE_REPO": "Lykon/dreamshaper-8",
        "CONTROL_MODEL_REPO": "xinsir/controlnet-union-sdxl-1.0",
        "DATASET_REPO": "Bakobiibizo/train14",
        "IS_VALIDATOR": True,
        "CACHE_PATH": "image_cache",
        "CACHE_SIZE": 40 * 1024**2,
        "CHECKPOINT_PATH": "models/sam_vit_l_0b3195.pth",
        "MODEL_TYPE": "vit_l",
        "MODELS_CACHE": "models_cache",
        "PRIOR_STEPS": 25,
        "PRIOR_GUIDANCE_SCALE": 1.0,
        "SYNTHETIC_ENDPOINT_PREFIX": "synthetic",
        "CHECKING_ENDPOINT_PREFIX": "checking",
        "OUTGOING": "Outgoing",
        "SINGULAR_GPU": "",
        "HOTKEY_PARAM": "bako_hot",
        "IMAGE_WORKER_URL_PARAM": "http://100.64.221.101:8188/prompt",
        "MIXTRAL_TEXT_WORKER_URL_PARAM": "http://100.117.156.73:7099/v1/chat/completions",
        "LLAMA_3_TEXT_WORKER_URL_PARAM": "http:100.117.156.73/v1/chat/completions",
        "TRANSLATION_WORKER_URL_PARAM": "http://100.77.94.60:4269/translate",
        "SAFETY_CHECKERS_PARAM": "cuda:0",
        "CLIP_DEVICE_PARAM": "cuda:1",
        "SCRIBBLE_DEVICE_PARAM": "cuda:2",
        "KANDINSKY_DEVICE_PARAM": "cuda:3",
        "SDXL_TURBO_DEVICE_PARAM": "cuda:4",
        "UPSCALE_DEVICE_PARAM": "cuda:5",
        "WALLET_NAME_PARAM": "bako_vali",
        "SUBTENSOR_NETWORK_PARAM": "finney",
        "SUBTENSOR_CHAINENDPOINT_PARAM": "entrypoint-finney.opentensor.ai",
        "IS_VALIDATOR_PARAM": True,
        "API_SERVER_PORT_PARAM": 4267,
        "EXTERNAL_SERVER_ADDRESS_PARAM": "172.17.0.1",
        "AXON_PORT_PARAM": 4269,
        "AXON_EXTERNAL_IP_PARAM": "172.17.0.1",
        "VISION_DB": "vision_database.db",
    }
)


class CONSTANTS(Enum):
    SCORING_PERIOD_TIME = constant_obj.SCORING_PERIOD_TIME
    SEED_CHUNK_SIZE = constant_obj.SEED_CHUNK_SIZE
    TASK_CONFIG_JSON = constant_obj.TASK_CONFIG_JSON
    TASK_CONCURRENCY_CONFIG_JSON = constant_obj.TASK_CONCURRENCY_CONFIG_JSON
    BLOCKS_PER_EPOCH = constant_obj.BLOCKS_PER_EPOCH
    BLOCK_TIME_IN_S = constant_obj.BLOCK_TIME_IN_S
    SPECIAL_CONCEPTS = constant_obj.SPECIAL_CONCEPTS
    NSFW_CONCEPTS = constant_obj.NSFW_CONCEPTS
    NSFW_RESPONSE_ERROR = constant_obj.NSFW_RESPONSE_ERROR
    LUNA_DIFFUSION_REPO = constant_obj.LUNA_DIFFUSION_REPO
    DEFAULT_NEGATIVE_PROMPT = constant_obj.DEFAULT_NEGATIVE_PROMPT
    KANDINKSY_NEGATIVE_PROMPT_PERFIX = constant_obj.KANDINKSY_NEGATIVE_PROMPT_PERFIX
    LARGEST_SEED = constant_obj.LARGEST_SEED
    DEFAULT_CFG_SCALE = constant_obj.DEFAULT_CFG_SCALE
    DEFAULT_HEIGHT = constant_obj.DEFAULT_HEIGHT
    DEFAULT_WIDTH = constant_obj.DEFAULT_WIDTH
    DEFAULT_SAMPLES = constant_obj.DEFAULT_SAMPLES
    DEFAULT_STEPS = constant_obj.DEFAULT_STEPS
    DEFAULT_STYLE_PRESET = constant_obj.DEFAULT_STYLE_PRESET
    DEFAULT_IMAGE_STRENGTH = constant_obj.DEFAULT_IMAGE_STRENGTH
    DEFAULT_INIT_IMAGE_MODE = constant_obj.DEFAULT_INIT_IMAGE_MODE
    DEFAULT_SAMPLER = constant_obj.DEFAULT_SAMPLER
    DEFAULT_ENGINE = constant_obj.DEFAULT_ENGINE
    UPSCALE_ENGINE = constant_obj.UPSCALE_ENGINE
    ALLOWED_IMAGE_SIZES = constant_obj.ALLOWED_IMAGE_SIZES
    DEBUG_MINER_PARAM = constant_obj.DEBUG_MINER_PARAM
    MODEL_CLIP = constant_obj.MODEL_CLIP
    AVAILABLE_TASKS_OPERATION = constant_obj.AVAILABLE_TASKS_OPERATION
    MODEL_SDXL_TURBO = constant_obj.MODEL_SDXL_TURBO
    MODEL_SCRIBBLE = constant_obj.MODEL_SCRIBBLE
    MODEL_MARKOV = constant_obj.MODEL_MARKOV
    MODEL_CACHE = constant_obj.MODEL_CACHE
    MODEL_UPSCALE = constant_obj.MODEL_UPSCALE
    PROMPT_SAFETY_CHECKERS = constant_obj.PROMPT_SAFETY_CHECKERS
    IMAGE_SAFETY_CHECKERS = constant_obj.IMAGE_SAFETY_CHECKERS
    DEVICE_DEFAULT = constant_obj.DEVICE_DEFAULT
    CONFIG_FILEPATH = constant_obj.CONFIG_FILEPATH
    OPERATION_TEXT_TO_IMAGE = constant_obj.OPERATION_TEXT_TO_IMAGE
    OPERATION_IMAGE_TO_IMAGE = constant_obj.OPERATION_IMAGE_TO_IMAGE
    OPERATION_INPAINT = constant_obj.OPERATION_INPAINT
    OPERATION_UPSCALE = constant_obj.OPERATION_UPSCALE
    OPERATION_SEGMENT = constant_obj.OPERATION_SEGMENT
    OPERATION_CLIP_EMBEDDINGS = constant_obj.OPERATION_CLIP_EMBEDDINGS
    OPERATION_SCRIBBLE = constant_obj.OPERATION_SCRIBBLE
    OPERATION_TRANSLATION = constant_obj.OPERATION_TRANSLATION
    CLIP_MODEL_REPO = constant_obj.CLIP_MODEL_REPO
    DREAMSHAPER_XL_LOCAL_FILE = constant_obj.DREAMSHAPER_XL_LOCAL_FILE
    KANDINSKY_PIPELINE_REPO = constant_obj.KANDINSKY_PIPELINE_REPO
    INPAINT_PIPELINE_REPO = constant_obj.INPAINT_PIPELINE_REPO
    DREAMSHAPER_PIPELINE_REPO = constant_obj.DREAMSHAPER_PIPELINE_REPO
    CONTROL_MODEL_REPO = constant_obj.CONTROL_MODEL_REPO
    DATASET_REPO = constant_obj.DATASET_REPO
    IS_VALIDATOR = constant_obj.IS_VALIDATOR
    CACHE_PATH = constant_obj.CACHE_PATH
    CACHE_SIZE = constant_obj.CACHE_SIZE
    CHECKPOINT_PATH = constant_obj.CHECKPOINT_PATH
    MODEL_TYPE = constant_obj.MODEL_TYPE
    MODELS_CACHE = constant_obj.MODELS_CACHE
    PRIOR_STEPS = constant_obj.PRIOR_STEPS
    PRIOR_GUIDANCE_SCALE = constant_obj.PRIOR_GUIDANCE_SCALE
    SYNTHETIC_ENDPOINT_PREFIX = constant_obj.SYNTHETIC_ENDPOINT_PREFIX
    CHECKING_ENDPOINT_PREFIX = constant_obj.CHECKING_ENDPOINT_PREFIX
    OUTGOING = constant_obj.OUTGOING
    SINGULAR_GPU = constant_obj.SINGULAR_GPU
    HOTKEY_PARAM = constant_obj.HOTKEY_PARAM
    IMAGE_WORKER_URL_PARAM = constant_obj.IMAGE_WORKER_URL_PARAM
    MIXTRAL_TEXT_WORKER_URL_PARAM = constant_obj.MIXTRAL_TEXT_WORKER_URL_PARAM
    LLAMA_3_TEXT_WORKER_URL_PARAM = constant_obj.LLAMA_3_TEXT_WORKER_URL_PARAM
    TRANSLATION_WORKER_URL_PARAM = constant_obj.TRANSLATION_WORKER_URL_PARAM
    SAFETY_CHECKERS_PARAM = constant_obj.SAFETY_CHECKERS_PARAM
    CLIP_DEVICE_PARAM = constant_obj.CLIP_DEVICE_PARAM
    SCRIBBLE_DEVICE_PARAM = constant_obj.SCRIBBLE_DEVICE_PARAM
    KANDINSKY_DEVICE_PARAM = constant_obj.KANDINSKY_DEVICE_PARAM
    SDXL_TURBO_DEVICE_PARAM = constant_obj.SDXL_TURBO_DEVICE_PARAM
    UPSCALE_DEVICE_PARAM = constant_obj.UPSCALE_DEVICE_PARAM
    WALLET_NAME_PARAM = constant_obj.WALLET_NAME_PARAM
    SUBTENSOR_NETWORK_PARAM = constant_obj.SUBTENSOR_NETWORK_PARAM
    SUBTENSOR_CHAINENDPOINT_PARAM = constant_obj.SUBTENSOR_CHAINENDPOINT_PARAM
    IS_VALIDATOR_PARAM = constant_obj.IS_VALIDATOR_PARAM
    API_SERVER_PORT_PARAM = constant_obj.API_SERVER_PORT_PARAM
    EXTERNAL_SERVER_ADDRESS_PARAM = constant_obj.EXTERNAL_SERVER_ADDRESS_PARAM
    AXON_PORT_PARAM = constant_obj.AXON_PORT_PARAM
    AXON_EXTERNAL_IP_PARAM = constant_obj.AXON_EXTERNAL_IP_PARAM
    VISION_DB = constant_obj.VISION_DB


for key in CONSTANTS:
    set_key("./.env", key.name, key.value)

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
    core_cst.HOTKEY_PARAM: {
        "default": CONSTANTS.HOTKEY_PARAM,
        "message": "Hotkey name: ",
    },
}

MISC_PARAMETERS = {
    core_cst.WALLET_NAME_PARAM: {
        "default": CONSTANTS.WALLET_NAME_PARAM,
        "message": "Wallet Name ",
    },
    core_cst.SUBTENSOR_NETWORK_PARAM: {
        "default": CONSTANTS.SUBTENSOR_NETWORK_PARAM,
        "message": "Subtensor Network (finney, test, local)",
    },
    core_cst.SUBTENSOR_CHAINENDPOINT_PARAM: {
        "default": CONSTANTS.SUBTENSOR_CHAINPOINT_PARAM,
        "message": "Subtensor Chain Endpoint ",
    },
    core_cst.IS_VALIDATOR_PARAM: {
        "default": CONSTANTS.IS_VALIDATOR_PARAM,
        "message": "Is this a Validator hotkey? (y/n) ",
        "process_function": bool_processing_func,
    },
}

VALIDATOR_PARAMETERS = {
    core_cst.API_SERVER_PORT_PARAM: {
        "default": CONSTANTS.API_SERVER_PORT_PARAM,
        "message": "API server port (if you're running an organic validator, else leave it)",
    },
    core_cst.EXTERNAL_SERVER_ADDRESS_PARAM: {
        "default": CONSTANTS.EXTERNAL_SERVER_ADDRESS_PARAM,
        "message": "External Server Address: ",
        "process_function": http_address_processing_func,
    },
}

MINER_PARAMETERS = {
    core_cst.AXON_PORT_PARAM: {
        "default": CONSTANTS.AXON_PORT_PARAM,
        "message": "Axon Port: ",
    },
    core_cst.AXON_EXTERNAL_IP_PARAM: {
        "default": CONSTANTS.AXON_EXTERNAL_IP_PARAM,
        "message": "Axon External IP: ",
    },
    core_cst.IMAGE_WORKER_URL_PARAM: {
        "default": CONSTANTS.IMAGE_WORKER_URL_PARAM,
        "message": "Image Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.MIXTRAL_TEXT_WORKER_URL_PARAM: {
        "default": CONSTANTS.MIXTRAL_TEXT_WORKER_URL_PARAM,
        "message": "Mixtral Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.LLAMA_3_TEXT_WORKER_URL_PARAM: {
        "default": CONSTANTS.LLAMA_3_TEXT_WORKER_URL_PARAM,
        "message": "Llama 3 Text Worker URL: ",
        "process_function": optional_http_address_processing_func,
    },
    core_cst.TRANSLATION_WORKER_URL_PARAM: {
        "default": CONSTANTS.TRANSLATION_WORKER_URL_PARAM,
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
