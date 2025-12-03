# Dublador IA – Whisper + XTTS v2

Pipeline de dublagem por IA usando:

- [OpenAI Whisper](https://github.com/openai/whisper) para transcrição
- [XTTS v2](https://github.com/coqui-ai/TTS) para dublagem com clonagem de voz

> Prova de conceito de dublagem automática: transcreve o áudio original, salva as legendas em TXT e gera um novo áudio dublado em outro idioma, preservando o timbre da voz original.

---

## ✨ Funcionalidades

- Transcrição automática de áudio (Whisper `large-v3` por padrão)
- Salvamento de legendas em `.txt` (com timestamps)
- Geração de áudio dublado usando XTTS v2
- Suporte a GPU (CUDA / RTX)
- CLI com 3 modos:
  - `transcribe` – só transcreve
  - `dub` – só dublagem a partir de TXT
  - `full` – transcreve + dubla em uma chamada

---

## ⚙️ Requisitos

- Python 3.10+
- GPU NVIDIA com suporte a CUDA (testado com RTX 3090, CUDA 12.1)
- Drivers atualizados

---

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/whisper-xtts-dubber.git
cd whisper-xtts-dubber

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt
