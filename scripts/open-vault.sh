#!/bin/zsh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Prefer the standard macOS app launcher so this works even when
# Obsidian's internal command-line interface setting is disabled.
open -a Obsidian "$ROOT_DIR"
