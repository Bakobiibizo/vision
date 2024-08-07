from typing import List, Tuple


SCORING_PERIOD_TIME = 60 * 60  # 0.5

SEED_CHUNK_SIZE = 100_000


TASK_CONFIG_JSON = "task_config.json"
TASK_CONCURRENCY_CONFIG_JSON = "task_concurrency_config.json"
BLOCKS_PER_EPOCH = 360
BLOCK_TIME_IN_S = 12


SPECIAL_CONCEPTS = [
    "little girl",
    "young child",
    "young girl",
    "little boy",
    "young boy",
]
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
NSFW_RESPONSE_ERROR = "error_nsfw_image"

LUNA_DIFFUSION_REPO = "proximasanfinetuning/luna-diffusion"

DEFAULT_NEGATIVE_PROMPT = ", ".join(NSFW_CONCEPTS) + ", worst quality, low quality"
KANDINKSY_NEGATIVE_PROMPT_PERFIX = "overexposed"

LARGEST_SEED = 4294967295
DEFAULT_CFG_SCALE = 7
DEFAULT_HEIGHT = 1024
DEFAULT_WIDTH = 1024
DEFAULT_SAMPLES = 1
DEFAULT_STEPS = 4
DEFAULT_STYLE_PRESET = None
DEFAULT_IMAGE_STRENGTH = 0.20
DEFAULT_INIT_IMAGE_MODE = "IMAGE_STRENGTH"
DEFAULT_SAMPLER = None
DEFAULT_ENGINE = "dreamshaperxlalpha"
UPSCALE_ENGINE = "esrgan-v1-x2plus"

ALLOWED_IMAGE_SIZES: List[Tuple[int, int]] = [
    (1024, 1024),
    (1152, 896),
    (1216, 832),
    (1344, 768),
    (1536, 640),
    (640, 1536),
    (768, 1344),
    (832, 1216),
    (896, 1152),
]

DEBUG_MINER_PARAM = "debug_miner"

MODEL_CLIP = "clip"


AVAILABLE_TASKS_OPERATION = "available_tasks_operation"

MODEL_SDXL_TURBO = "sdxl_turbo"
MODEL_SCRIBBLE = "scribble"
MODEL_MARKOV = "markov"
MODEL_CACHE = "cache"
MODEL_UPSCALE = "upscale"

PROMPT_SAFETY_CHECKERS = "prompt_safety_checkers"
IMAGE_SAFETY_CHECKERS = "image_safety_checkers"


DEVICE_DEFAULT = "cuda"


CONFIG_FILEPATH = "config.yaml"


OPERATION_TEXT_TO_IMAGE = "TextToImage"
OPERATION_IMAGE_TO_IMAGE = "ImageToImage"
OPERATION_INPAINT = "Inpaint"
OPERATION_UPSCALE = "Upscale"
OPERATION_SEGMENT = "Segment"
OPERATION_CLIP_EMBEDDINGS = "ClipEmbeddings"
OPERATION_SCRIBBLE = "Scribble"
OPERATION_TRANSLATION = "Translation"


CLIP_MODEL_REPO = "laion/CLIP-ViT-bigG-14-laion2B-39B-b160k"
DREAMSHAPER_XL_LOCAL_FILE = "dreamshaperxlalpha.safetensors"
KANDINSKY_PIPELINE_REPO = "kandinsky-community/kandinsky-2-2-decoder"
INPAINT_PIPELINE_REPO = "kandinsky-community/kandinsky-2-2-decoder-inpaint"
DREAMSHAPER_PIPELINE_REPO = "Lykon/dreamshaper-8"
CONTROL_MODEL_REPO = "xinsir/controlnet-union-sdxl-1.0"
DATASET_REPO = "Bakobiibizo/train14"

IS_VALIDATOR = "is_validator"

CACHE_PATH = "image_cache"
CACHE_SIZE = 40 * 1024**2  # 40mb, just something small for the validator

CHECKPOINT_PATH = "models/sam_vit_l_0b3195.pth"
MODEL_TYPE = "vit_l"


# If you change this, please change the git ignore too
MODELS_CACHE = "models_cache"

# Kandinsky params

PRIOR_STEPS = 25
PRIOR_GUIDANCE_SCALE = 1.0

SYNTHETIC_ENDPOINT_PREFIX = "synthetic"
CHECKING_ENDPOINT_PREFIX = "checking"
OUTGOING = "Outgoing"

SINGULAR_GPU = ""

HOTKEY_PARAM = "bako_hot"


IMAGE_WORKER_URL_PARAM = "http://100.64.221.101:8188/prompt"
MIXTRAL_TEXT_WORKER_URL_PARAM = "text-agentartificial.ngrok.app/v1/chat/completions"
LLAMA_3_TEXT_WORKER_URL_PARAM = "text-agentartificial.ngrok.app/v1/chat/completions"
TRANSLATION_WORKER_URL_PARAM = "https://"

SAFETY_CHECKERS_PARAM = "cuda:0"
CLIP_DEVICE_PARAM = "cuda:0"
SCRIBBLE_DEVICE_PARAM = "cuda:0"
KANDINSKY_DEVICE_PARAM = "cuda:1"
SDXL_TURBO_DEVICE_PARAM = "cuda:2"
UPSCALE_DEVICE_PARAM = "cuda:4"

WALLET_NAME_PARAM = "bako_vali"
SUBTENSOR_NETWORK_PARAM = "finney"
SUBTENSOR_CHAINENDPOINT_PARAM = "entrypoint-finney.opentensor.ai"
IS_VALIDATOR_PARAM = "True"
API_SERVER_PORT_PARAM = "4267"
EXTERNAL_SERVER_ADDRESS_PARAM = "192.168.0.152"
AXON_PORT_PARAM = "4269"
AXON_EXTERNAL_IP_PARAM = "192.168.0.152"



VISION_DB = "vision_database.db"
