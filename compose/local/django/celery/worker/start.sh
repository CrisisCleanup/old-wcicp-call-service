#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


C_FORCE_ROOT=true celery -A crisiscleanup.taskapp worker -l DEBUG
