<#
.SYNOPSIS
    Automated first-run setup for the NHS Service Tracker Flask project.
.DESCRIPTION
    Creates a Python virtual environment, installs dependencies,
    generates a secure SECRET_KEY, initialises the database,
    seeds roles and an admin user, and launches the Flask dev server.
#>

Write-Host "=== NHS Service Tracker: Automated Setup (Windows PowerShell) ===" -ForegroundColor Cyan
$ErrorActionPreference = "Stop"

# 1️⃣  Create venv
if (!(Test-Path ".\.venv")) {
    Write-Host "[1/7] Creating Python virtual environment (.venv)..." -ForegroundColor Yellow
    python -m venv .venv
} else {
    Write-Host "[1/7] Virtual environment already exists, skipping." -ForegroundColor Gray
}

# 2️⃣  Activate venv for this session
Write-Host "[2/7] Activating virtual environment..." -ForegroundColor Yellow
$activate = ".\.venv\Scripts\Activate.ps1"
. $activate

# 3️⃣  Install requirements
Write-Host "[3/7] Installing Python dependencies..." -ForegroundColor Yellow
pip install --upgrade pip
pip install -r requirements.txt

# 4️⃣  Create .env with secure key
if (!(Test-Path ".\.env")) {
    Write-Host "[4/7] Creating .env from .env.example..." -ForegroundColor Yellow
    Copy-Item ".\.env.example" ".\.env"

    $secret = python - << 'PY'
import secrets
print(secrets.token_hex(32))
PY

    (Get-Content .\.env) `
        -replace 'SECRET_KEY=change-me', ("SECRET_KEY=" + $secret.Trim()) `
        | Set-Content .\.env
} else {
    Write-Host "[4/7] .env already exists, skipping." -ForegroundColor Gray
}

Write-Host "`nCurrent .env contents:" -ForegroundColor DarkCyan
Get-Content .\.env
Write-Host "------`n"

# 5️⃣  Database init + migrate + upgrade
Write-Host "[5/7] Initialising / migrating database (SQLite by default)..." -ForegroundColor Yellow
try {
    flask --app wsgi db init
} catch {
    Write-Host "Migrations folder already exists." -ForegroundColor Gray
}
try {
    flask --app wsgi db migrate -m "init"
} catch {
    Write-Host "Migration already exists." -ForegroundColor Gray
}
flask --app wsgi db upgrade

# 6️⃣  Seed roles + admin account
Write-Host "[6/7] Seeding roles and default admin user..." -ForegroundColor Yellow
flask --app wsgi seed

# 7️⃣  Launch dev server
Write-Host "[7/7] Starting Flask dev server on http://127.0.0.1:5000 ..." -ForegroundColor Green
flask --app wsgi run
