#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A crisiscleanup.taskapp worker -l INFO
