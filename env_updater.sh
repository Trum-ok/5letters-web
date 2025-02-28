#!/bin/bash

if [ -f .env ]; then
    echo ".env file found"
    export $(grep -v '^#' .env | xargs)
fi