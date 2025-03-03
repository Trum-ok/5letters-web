#!/usr/bin/env sh

set -e


# if [ -z "$ELASTICSEARCH_PORT" ]; then
#     echo "Error: ELASTICSEARCH_PORT environment variable is not set."
#     exit 1
# fi

# if ! echo "$ELASTICSEARCH_PORT" | grep -qE '^[0-9]+$'; then
#   echo "Error: Invalid ELASTICSEARCH_PORT format." >&2
#   exit 1
# fi

FILEBEAT_FILE="/usr/share/filebeat/filebeat.tpl.yml"

if [ ! -f $FILEBEAT_FILE ]; then
    echo "Error: filebeat.tpl.yml file not found at $FILEBEAT_FILE" >&2
    exit 1
fi

# if ! envsubst < /usr/share/filebeat/filebeat.tpl.yml > /usr/share/filebeat/filebeat.yml; then
#   echo "Error: Failed to generate filebeat.yml" >&2
#   exit 1
# fi

envsubst < /usr/share/filebeat/filebeat.tpl.yml > /usr/share/filebeat/filebeat.yml

if [ ! -s "/usr/share/filebeat/filebeat.yml" ]; then
  echo "Error: Generated filebeat.yml is empty" >&2
  exit 1
fi

exec filebeat -e
