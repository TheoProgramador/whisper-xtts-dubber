from pathlib import Path

# Modelos
WHISPER_MODEL = "large-v3"
XTTS_MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"

# Padrões de arquivos
DEFAULT_TXT = "legendas.txt"
DEFAULT_OUTPUT = "audio_dublado.wav"

# Limite seguro de caracteres por bloco (XTTS avisa em ~203)
MAX_CHARS_PT = 180

PROJECT_ROOT = Path(__file__).resolve().parent.parent
