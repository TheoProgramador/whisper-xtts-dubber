# whisper-xtts-dubber
Dublador IA – Whisper + XTTS v2

Este projeto é uma prova de conceito de dublagem automatizada utilizando modelos modernos de inteligência artificial.
A pipeline combina:
Transcrição neural (Whisper large-v3)
Modelagem e clonagem de voz (XTTS v2)
Síntese avançada de fala
Geração de áudio final totalmente automatizada
O objetivo é demonstrar como tecnologias atuais podem adaptar conteúdos para outros idiomas, mantendo naturalidade, clareza e fluidez — tudo de forma prática, modular e extensível.

Recursos Principais

Transcrição automática de áudio com Whisper
Salvamento de legendas com timestamps em .txt
Clonagem de voz por IA usando poucos segundos da voz original
Dublagem gerada via XTTS v2 com entonação natural
Junção automática dos blocos de áudio
Interface de linha de comando com três modos:
transcribe – apenas transcreve
dub – apenas dublagem a partir de TXT
full – pipeline completa (transcrever + dublar)

Arquitetura

O projeto é organizado em módulos independentes:
transcription.py – transcrição e exportação de legendas
dubbing.py – geração da dublagem neural
cli.py – interface de linha de comando
config.py – configurações gerais do pipeline
Essa estrutura facilita evolução, customização e integração com outros sistemas.

Uso
Transcrição
python -m dublador_ia.cli transcribe --audio audio_original.wav

Dublagem
python -m dublador_ia.cli dub --audio audio_original.wav

Pipeline Completa
python -m dublador_ia.cli full --audio audio_original.wav

Propósito
Este repositório serve como ponto de partida para quem deseja:
Explorar dublagem por IA
Criar ferramentas de acessibilidade
Estudar modelos de síntese neural de voz
Integrar transcrição + dublagem em fluxos multimídia
Entender pipelines modernas de IA voltadas para áudio

Aviso Legal
Este projeto tem caráter educacional e de demonstração tecnológica.
Respeite direitos autorais e políticas de uso ao processar conteúdos de terceiros.

Créditos
Projeto desenvolvido por Theo Miliani.
Tecnologias baseadas em Whisper (OpenAI) e XTTS (Coqui TTS).
