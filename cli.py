import argparse
from pathlib import Path

from .config import DEFAULT_TXT, DEFAULT_OUTPUT
from .transcription import transcrever_audio, salvar_legendas_txt, carregar_legendas_txt
from .dubbing import gerar_dublagem


def cmd_transcribe(args):
    segments = transcrever_audio(
        audio_path=args.audio,
        model_name=args.model,
        language=args.language,
    )
    salvar_legendas_txt(segments, args.out)


def cmd_dub(args):
    segments = carregar_legendas_txt(args.legendas)
    gerar_dublagem(
        segments=segments,
        speaker_wav=args.speaker or args.audio,
        out_path=args.out,
        language=args.language,
        speed=args.speed,
    )


def cmd_full(args):
    segments = transcrever_audio(
        audio_path=args.audio,
        model_name=args.model,
        language=args.language_in,
    )
    salvar_legendas_txt(segments, args.legendas)

    gerar_dublagem(
        segments=segments,
        speaker_wav=args.speaker or args.audio,
        out_path=args.out,
        language=args.language_out,
        speed=args.speed,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dublador-ia",
        description="Pipeline de dublagem por IA (Whisper + XTTS v2).",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # sub: transcribe
    p_trans = sub.add_parser("transcribe", help="Apenas transcreve o áudio e gera um TXT.")
    p_trans.add_argument("--audio", required=True, help="Arquivo de áudio de entrada.")
    p_trans.add_argument("--model", default="large-v3", help="Modelo Whisper (ex: tiny, base, small, medium, large-v3).")
    p_trans.add_argument("--language", default="en", help="Idioma do áudio de entrada (ou None para autodetect).")
    p_trans.add_argument("--out", default=DEFAULT_TXT, help="Arquivo TXT de saída.")
    p_trans.set_defaults(func=cmd_transcribe)

    # sub: dub
    p_dub = sub.add_parser("dub", help="Apenas gera a dublagem a partir de um TXT existente.")
    p_dub.add_argument("--audio", required=True, help="Áudio original (usado como referência se speaker não for informado).")
    p_dub.add_argument("--legendas", default=DEFAULT_TXT, help="Arquivo TXT de legendas.")
    p_dub.add_argument("--speaker", help="Áudio de referência da voz (default = o próprio áudio original).")
    p_dub.add_argument("--out", default=DEFAULT_OUTPUT, help="Arquivo de áudio dublado de saída.")
    p_dub.add_argument("--language", default="pt", help="Idioma da dublagem.")
    p_dub.add_argument("--speed", type=float, default=0.95, help="Velocidade da fala.")
    p_dub.set_defaults(func=cmd_dub)

    # sub: full
    p_full = sub.add_parser("full", help="Transcreve e dubla em uma única chamada.")
    p_full.add_argument("--audio", required=True, help="Áudio original.")
    p_full.add_argument("--model", default="large-v3", help="Modelo Whisper.")
    p_full.add_argument("--language-in", default="en", help="Idioma do áudio original.")
    p_full.add_argument("--language-out", default="pt", help="Idioma da dublagem.")
    p_full.add_argument("--legendas", default=DEFAULT_TXT, help="Arquivo TXT intermediário.")
    p_full.add_argument("--speaker", help="Áudio de referência da voz.")
    p_full.add_argument("--out", default=DEFAULT_OUTPUT, help="Arquivo de áudio dublado.")
    p_full.add_argument("--speed", type=float, default=0.95, help="Velocidade da fala.")
    p_full.set_defaults(func=cmd_full)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
