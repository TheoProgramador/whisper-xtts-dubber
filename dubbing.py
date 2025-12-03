from pathlib import Path
from typing import Sequence

from pydub import AudioSegment
from TTS.api import TTS

from .config import XTTS_MODEL, MAX_CHARS_PT, DEFAULT_OUTPUT


def _split_text(text: str, max_len: int = MAX_CHARS_PT) -> list[str]:
    """
    Quebra o texto em blocos menores respeitando o limite de caracteres.
    """
    blocks: list[str] = []
    text = text.strip()

    while len(text) > max_len:
        cut = text.rfind(" ", 0, max_len)
        if cut == -1:
            cut = max_len
        blocks.append(text[:cut].strip())
        text = text[cut:].strip()

    if text:
        blocks.append(text)

    return blocks


def gerar_dublagem(
    segments: Sequence[dict],
    speaker_wav: str | Path,
    out_path: str | Path = DEFAULT_OUTPUT,
    language: str = "pt",
    speed: float = 0.95,
):
    """
    Gera um arquivo de áudio dublado a partir dos segmentos transcritos.
    Usa XTTS v2 com voz clonada do speaker_wav.
    """
    speaker_wav = Path(speaker_wav)
    out_path = Path(out_path)

    if not speaker_wav.exists():
        raise FileNotFoundError(f"Áudio de referência não encontrado: {speaker_wav}")

    # Junta todo o texto numa sequência só.
    full_text = " ".join(seg["text"] for seg in segments)
    blocks = _split_text(full_text, MAX_CHARS_PT)

    print(f"[XTTS] Texto dividido em {len(blocks)} blocos.")

    print(f"[XTTS] Carregando modelo: {XTTS_MODEL}")
    tts = TTS(model_name=XTTS_MODEL)
    tts.to("cuda")

    # Áudio final
    final_audio = AudioSegment.silent(duration=0)

    for i, block in enumerate(blocks):
        tmp_path = out_path.with_name(f"{out_path.stem}_part_{i}.wav")
        print(f"[XTTS] Renderizando bloco {i+1}/{len(blocks)}...")

        tts.tts_to_file(
            text=block,
            speaker_wav=str(speaker_wav),
            language=language,
            speed=speed,
            split_sentences=True,
            file_path=str(tmp_path),
        )

        final_audio += AudioSegment.from_wav(tmp_path)

    final_audio.export(out_path, format="wav")
    print(f"[XTTS] Áudio dublado salvo em: {out_path}")
    return out_path
