#!/bin/bash
# Installe la chaîne d'outils HyperFrames (rendu vidéo, transcription,
# voix off et musique locales) au démarrage d'une session cloud.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Chrome headless utilisé par HyperFrames pour le rendu
npx -y hyperframes browser ensure > /dev/null

# whisper.cpp (transcription / sous-titres), compilé là où HyperFrames le cherche
WHISPER_DIR="$HOME/.cache/hyperframes/whisper/whisper.cpp"
WHISPER_BIN="$WHISPER_DIR/build/bin/whisper-cli"
if [ ! -x "$WHISPER_BIN" ]; then
  rm -rf "$WHISPER_DIR"
  mkdir -p "$(dirname "$WHISPER_DIR")"
  git clone -q --depth 1 https://github.com/ggml-org/whisper.cpp "$WHISPER_DIR"
  cmake -S "$WHISPER_DIR" -B "$WHISPER_DIR/build" \
    -DCMAKE_BUILD_TYPE=Release -DWHISPER_BUILD_TESTS=OFF > /dev/null
  cmake --build "$WHISPER_DIR/build" -j"$(nproc)" --config Release --target whisper-cli > /dev/null
fi
ln -sf "$WHISPER_BIN" /usr/local/bin/whisper-cli

# Kokoro (voix off locale) et MusicGen (musique locale), PyTorch en version CPU
if ! python3 -c "import kokoro_onnx, soundfile, torch, transformers, numpy" 2> /dev/null; then
  pip install -q --root-user-action=ignore kokoro-onnx soundfile
  pip install -q --root-user-action=ignore --index-url https://download.pytorch.org/whl/cpu torch
  pip install -q --root-user-action=ignore transformers numpy
fi
