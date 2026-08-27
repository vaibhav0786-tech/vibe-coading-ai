# Ollama Model Registration

The actual GGUF files will be registered on the cloud GPU machine.

Expected source models:

1. DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf
2. mmproj-Devstral-Small-2-24B-Instruct-2512-F16.gguf
3. qwen3-4b-thinking-2507.Q4_K_M.gguf

Do not copy the large model files into Git.

They will be uploaded separately to the cloud GPU server.

Each model will receive its own Ollama Modelfile.

The orchestration gateway will select the appropriate model based on task type.
