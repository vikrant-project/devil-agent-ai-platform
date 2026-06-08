# Devil Agent Configuration Summary

## System Information
- **VPS IP:** 13.62.57.154
- **Domain:** devils.your-domain.com
- **Working Directory:** /home/ubuntu/devils-agent
- **Devil Home:** /home/ubuntu/.devil
- **Python:** 3.11.0rc1

## API Server
- **Port:** 9241
- **Host:** 0.0.0.0
- **URL:** http://13.62.57.154:9241 or https://devils.your-domain.com
- **API Key:** 0b9f8387a15913bbd6712b4eb205d395374b6cd0373cd94cfc6785698841e0e0

## Endpoints
- Health: GET /health
- Models: GET /v1/models
- Chat Completions: POST /v1/chat/completions
- Capabilities: GET /v1/capabilities

## CLI Commands
- devil chat - Start interactive chat
- devil doctor - System health check
- devil sessions list - List sessions
- devil --help - Full help

## Service Management
- Start: sudo systemctl start devil-gateway
- Stop: sudo systemctl stop devil-gateway
- Status: sudo systemctl status devil-gateway
- Logs: tail -f /home/ubuntu/.devil/logs/gateway.log

## NVIDIA API Note
The NVIDIA API key requires model activation in the NVIDIA console.
Visit https://build.nvidia.com/ to activate:
- nvidia/llama-3.1-nemotron-70b-instruct
- nvidia/llama-3.3-70b-instruct

Once activated, the model will work with the devil CLI.

## Quick Start
```bash
# SSH into VPS
ssh -i devils.pem ubuntu@13.62.57.154

# Run Devil Agent CLI
devil chat

# Or use the API
curl -H "Authorization: Bearer 0b9f8387a15913bbd6712b4eb205d395374b6cd0373cd94cfc6785698841e0e0" http://13.62.57.154:9241/v1/models
```
