# Vibe Coding AI — Cloud Deployment Checklist

## Laptop
- [x] Python environment
- [x] FastAPI gateway
- [x] Task classifier
- [x] Fallback router
- [x] Aider environment
- [x] Continue configuration
- [x] Tests
- [x] Ruff
- [x] Cloud configuration
- [x] Ollama deployment templates

## Cloud GPU

### Infrastructure
- [ ] Rent GPU instance
- [ ] Install NVIDIA drivers
- [ ] Verify GPU with nvidia-smi
- [ ] Install Docker
- [ ] Install Ollama
- [ ] Configure firewall

### Models
- [ ] Upload DeepSeek-Coder-V2 GGUF
- [ ] Upload Qwen3 GGUF
- [ ] Upload Devstral main GGUF
- [ ] Upload Devstral mmproj GGUF
- [ ] Create coding Ollama model
- [ ] Create reasoning Ollama model
- [ ] Create vision Ollama model
- [ ] Verify all models load

### Services
- [ ] Start Ollama
- [ ] Start Vibe Coding Gateway
- [ ] Start OpenWebUI
- [ ] Configure API authentication
- [ ] Configure HTTPS/VPN
- [ ] Configure Aider
- [ ] Configure Continue

### Validation
- [ ] Gateway health check
- [ ] Ollama health check
- [ ] Coding route
- [ ] Reasoning route
- [ ] Vision route
- [ ] Fallback route
- [ ] Error handling
- [ ] Logging

### Production
- [ ] Persistent model storage
- [ ] Automatic service restart
- [ ] Cloud firewall
- [ ] Backups
- [ ] Monitoring
- [ ] Cost controls
