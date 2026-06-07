param(
    [string]$Message = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")
Set-Location -LiteralPath $repoRoot.Path

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if ([string]::IsNullOrWhiteSpace($Message)) {
    $Message = "Auto backup AI-Brain $timestamp"
}

$status = git status --porcelain

if ($status) {
    git add .
    git commit -m $Message
}
else {
    Write-Host "No local file changes to commit."
}

git push origin main

