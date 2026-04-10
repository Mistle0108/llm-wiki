#!/bin/zsh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if command -v obsidian >/dev/null 2>&1; then
  obsidian "$ROOT_DIR"
else
  open -a Obsidian "$ROOT_DIR"
fi
