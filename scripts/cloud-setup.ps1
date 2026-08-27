$ErrorActionPreference = "Stop"

Write-Host "=== Vibe Coding AI - Cloud Setup ==="

Write-Host "[1/5] Checking Docker..."
docker --version

Write-Host "[2/5] Checking Ollama..."
ollama --version

Write-Host "[3/5] Checking project directory..."
if (-not (Test-Path ".\app")) {
    throw "app directory not found."
}

Write-Host "[4/5] Checking deployment configuration..."
if (-not (Test-Path ".\config\.env.cloud.example")) {
    throw "Cloud environment template not found."
}

Write-Host "[5/5] Cloud setup prerequisites detected."
Write-Host ""
Write-Host "Next phase:"
Write-Host "1. Configure GPU server"
Write-Host "2. Install Ollama"
Write-Host "3. Register GGUF models"
Write-Host "4. Start gateway"
Write-Host "5. Connect Aider and Continue"
