[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw 'Python was not found. Install Python 3.10 or newer, then run this installer again.'
}

$codexRoot = Join-Path $env:USERPROFILE '.codex'
$targetDir = Join-Path $codexRoot 'mcp\apilio-image'
$targetServer = Join-Path $targetDir 'server.py'
$configPath = Join-Path $codexRoot 'config.toml'
$sourceServer = Join-Path $PSScriptRoot 'server.py'

if (-not (Test-Path -LiteralPath $sourceServer)) {
    throw "server.py is missing beside install.ps1: $sourceServer"
}

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
Copy-Item -LiteralPath $sourceServer -Destination $targetServer -Force

if (-not (Test-Path -LiteralPath $configPath)) {
    New-Item -ItemType File -Force -Path $configPath | Out-Null
}

$config = Get-Content -Raw -LiteralPath $configPath
if ($config -notmatch '(?m)^\[mcp_servers\.apilio_image\]\s*$') {
    $escapedServer = $targetServer.Replace('\', '\\')
    $block = @"

[mcp_servers.apilio_image]
command = "python"
args = ["$escapedServer"]
env_vars = ["APILIO_API_KEY"]
startup_timeout_sec = 30
tool_timeout_sec = 240
"@
    Add-Content -LiteralPath $configPath -Value $block -Encoding utf8
    Write-Host "Added apilio_image MCP configuration to $configPath"
} else {
    Write-Host 'The apilio_image MCP configuration already exists; it was preserved.'
    Write-Host "Verify that its args path points to: $targetServer"
}

$existingKey = [Environment]::GetEnvironmentVariable('APILIO_API_KEY', 'User')
if ([string]::IsNullOrWhiteSpace($existingKey)) {
    $secureKey = Read-Host 'Enter APILIO_API_KEY (input is hidden)' -AsSecureString
    $keyPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
    try {
        $plainKey = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($keyPointer)
        if ([string]::IsNullOrWhiteSpace($plainKey)) {
            throw 'No API key was entered.'
        }
        [Environment]::SetEnvironmentVariable('APILIO_API_KEY', $plainKey, 'User')
        $env:APILIO_API_KEY = $plainKey
    } finally {
        if ($keyPointer -ne [IntPtr]::Zero) {
            [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($keyPointer)
        }
        $plainKey = $null
        $secureKey = $null
    }
    Write-Host 'Saved APILIO_API_KEY as a Windows user environment variable.'
} else {
    Write-Host 'APILIO_API_KEY is already configured as a Windows user environment variable.'
}

& python -m py_compile $targetServer
if ($LASTEXITCODE -ne 0) {
    throw 'Python compilation check failed.'
}

Write-Host ''
Write-Host 'Installation finished.'
Write-Host 'Fully exit and restart Codex, then run the image-generation acceptance test.'
