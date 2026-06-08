#!/bin/bash
cd /home/ubuntu/devil_agent/agent_core
source .venv/bin/activate
export PYTHONPATH="/home/ubuntu/devil_agent/agent_core:$PYTHONPATH"
export DEVIL_HOME="/home/ubuntu/.devil"
set -a; source .env; set +a
exec python gateway/run.py --port 9241 --host 0.0.0.0
