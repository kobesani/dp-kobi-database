#!/bin/bash
set -eou pipefail

export DEVELOPMENT='TRUE'
poetry run python -m pytest --cov=dp_kobi_database tests -v "$@"
