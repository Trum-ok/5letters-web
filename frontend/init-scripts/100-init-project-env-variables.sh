#!/usr/bin/env sh

set -ex

if [ -z "$VITE_BACK_PORT" ]; then
    echo "Error: VITE_BACK_PORT environment variable is not set."
    exit 1
fi

ASSETS_DIR="/usr/share/nginx/html/assets"
ENV_FILE=$(ls -t "$ASSETS_DIR"/env-*.js 2>/dev/null | head -n1)

if [ -z "$ENV_FILE" ]; then
  echo "Error: env-*.js file not found in $ASSETS_DIR" >&2
  exit 1
fi

if [ -f "$ENV_FILE" ]; then
    sed -i.bak "s/__VITE_BACK_PORT__/$VITE_BACK_PORT/g" "$ENV_FILE" && rm -f "$ENV_FILE.bak"
    echo "Updated $ENV_FILE"
fi
