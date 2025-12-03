from pathlib import Path
import torch
import whisper
from .config import WHISPER_MODEL, DEFAULT_TXT


def transcrever_audio(audio_path: str | Path,
                      model_name: str = WHISPER_MODEL,
                      language: str | None = "en"):
    """
    Transcreve um arquivo de áudio usando Whisper e retorna a lista de segmentos.

    Cada segmento é um dict com: start, end, text.
    """
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Áudio não encontrado: {audio_path}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[Whisper] Carregando modelo {model_name} em {device}...")
    model = whisper.load_model(model_name, device=device)

    print(f"[Whisper] Transcrevendo: {audio_path.name}")
    result = model.transcribe(
        str(audio_path),
        task="transcribe",
        language=language  # None = auto-detecção
    )

    segments = result["segments"]
    print(f"[Whisper] {len(segments)} segmentos gerados.")
    return segments


def salvar_legendas_txt(segments, txt_path: str | Path = DEFAULT_TXT):
    """
    Salva os segmentos em um arquivo .txt num formato legível.
    """
    txt_path = Path(txt_path)
    with txt_path.open("w", encoding="utf-8") as f:
        for seg in segments:
            f.write(f"[{seg['start']:.2f} -> {seg['end']:.2f}] {seg['text']}\n")

    print(f"[TXT] Legendas salvas em: {txt_path}")
    return txt_path


def carregar_legendas_txt(txt_path: str | Path = DEFAULT_TXT):
    """
    Carrega segmentos a partir de um .txt gerado por salvar_legendas_txt.
    """
    txt_path = Path(txt_path)
    if not txt_path.exists():
        raise FileNotFoundError(f"Arquivo de legendas não encontrado: {txt_path}")

    segments = []
    with txt_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            tempo, texto = line.split("] ", 1)
            tempo = tempo.replace("[", "")
            start_str, end_str = tempo.split(" -> ")
            segments.append({
                "start": float(start_str),
                "end": float(end_str),
                "text": texto.strip()
            })

    print(f"[TXT] {len(segments)} segmentos carregados de {txt_path}")
    return segments
