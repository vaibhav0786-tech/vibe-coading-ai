# CLOUD DEPLOYMENT COMMAND REFERENCE

## Check GPU

nvidia-smi

## Check Ollama

ollama --version

## List models

ollama list

## Create coding model

ollama create vibe-coder -f Modelfile.coding

## Create reasoning model

ollama create vibe-reasoner -f Modelfile.reasoning

## Verify Ollama API

Invoke-WebRequest http://127.0.0.1:11434/api/tags

## Start Vibe Coding Gateway

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000

## Gateway health

Invoke-WebRequest http://127.0.0.1:8000/health

## IMPORTANT

Do not expose Ollama port 11434 directly to the public internet.

Prefer:
- Tailscale
- WireGuard
- SSH tunnel
- Private cloud network
- Reverse proxy with authentication
