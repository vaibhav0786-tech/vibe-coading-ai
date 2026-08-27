param(
    [string]$CloudHost = "127.0.0.1"
)

$ErrorActionPreference = "Stop"

Write-Host "=== Vibe Coding AI Cloud Health Check ==="
Write-Host "Target: $CloudHost"

Write-Host ""
Write-Host "[Ollama]"
try {
    $response = Invoke-WebRequest `
        -Uri "http://$CloudHost`:11434/api/tags" `
        -TimeoutSec 10 `
        -UseBasicParsing

    Write-Host "Ollama: OK ($($response.StatusCode))"
}
catch {
    Write-Host "Ollama: FAILED"
    Write-Host $_.Exception.Message
}

Write-Host ""
Write-Host "[Gateway]"
try {
    $response = Invoke-WebRequest `
        -Uri "http://$CloudHost`:8000/health" `
        -TimeoutSec 10 `
        -UseBasicParsing

    Write-Host "Gateway: OK ($($response.StatusCode))"
}
catch {
    Write-Host "Gateway: FAILED"
    Write-Host $_.Exception.Message
}

Write-Host ""
Write-Host "Health check complete."
