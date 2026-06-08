#!/bin/bash
cd /path/to/devil_agent/agent_core
source .venv/bin/activate
export PYTHONPATH="/path/to/devil_agent/agent_core:$PYTHONPATH"
export DEVIL_HOME="~/.devil"
set -a; source .env; set +a
exec python gateway/run.py --port 9241 --host 0.0.0.0
