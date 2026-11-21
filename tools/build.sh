#!/bin/bash
# Build the site into public/. Used by Cloudflare Workers Builds (build command: bash tools/build.sh)
# and works locally too. Installs Hugo extended and docutils (rst2html) when they are missing.
set -euo pipefail
HUGO_VERSION=${HUGO_VERSION:-0.146.5}
cd "$(dirname "$0")/.."
BIN="$PWD/.bin"
export PATH="$BIN:$HOME/.local/bin:$PATH"

if ! command -v hugo >/dev/null || ! hugo version | grep -q "v$HUGO_VERSION.*extended"; then
  mkdir -p "$BIN"
  case "$(uname -s)-$(uname -m)" in
    Linux-x86_64) asset=linux-amd64.tar.gz ;;
    Linux-aarch64) asset=linux-arm64.tar.gz ;;
    Darwin-*) asset=darwin-universal.tar.gz ;;
    *) echo "unsupported platform" >&2; exit 1 ;;
  esac
  curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_${asset}" \
    | tar -xz -C "$BIN" hugo
fi

if ! command -v rst2html >/dev/null && ! command -v rst2html.py >/dev/null; then
  python3 -m pip install --quiet --user docutils 2>/dev/null || python3 -m pip install --quiet docutils
fi

hugo version
hugo --cleanDestinationDir
