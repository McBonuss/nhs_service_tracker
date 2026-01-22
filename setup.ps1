<#
.SYNOPSIS
    Automated first-run setup for the NHS Service Tracker Django project.
.DESCRIPTION
    Creates a Python virtual environment, installs dependencies,
    generates a SECRET_KEY, initialises the database,
    seeds an admin user, and launches the Django dev server.
#>

Write-Host "=== NHS Service Tracker: Automated Setup (Windows PowerShell) ===" -ForegroundColor Cyan
$ErrorActionPreference = "Stop"

# 1. Create venv
if (!(Test-Path ".\.venv")) {
    Write-Host "[1/7] Creating Python virtual environment (.venv)..." -ForegroundColor Yellow
    python -m venv .venv
} else {
    Write-Host "[1/7] Virtual environment already exists, skipping." -ForegroundColor Gray
}

# 2. Activate venv for this session
Write-Host "[2/7] Activating virtual environment..." -ForegroundColor Yellow
$activate = ".\.venv\Scripts\Activate.ps1"
. $activate

# 3. Install requirements
Write-Host "[3/7] Installing Python dependencies..." -ForegroundColor Yellow
pip install --upgrade pip

# Create a filtered requirements list excluding PostgreSQL packages
$packages = Get-Content requirements.txt | Where-Object { $_ -notmatch '^#' -and $_.Trim() -ne '' -and $_ -notlike "psycopg2*" }
Write-Host "Skipping psycopg2-binary (PostgreSQL not needed for SQLite)" -ForegroundColor Yellow

# Install packages one by one for better error handling
foreach ($package in $packages) {
    try {
        pip install $package
        Write-Host "Installed: $package" -ForegroundColor Green
    } catch {
        Write-Host "Failed to install: $package" -ForegroundColor Red
        Write-Host "  Continuing with other packages..." -ForegroundColor Yellow
    }
}

# 4. Create env with key
if (!(Test-Path ".\env")) {
    Write-Host "[4/7] Creating env file with SECRET_KEY..." -ForegroundColor Yellow

    # Generate a key using Python
    $secret = python -c "import secrets; print(secrets.token_urlsafe(50))"

    $envContent = @"
DJANGO_SETTINGS_MODULE=nhs_service_tracker.settings
SECRET_KEY=$($secret.Trim())
DATABASE_URL=sqlite:///nhs_tracker.db
"@

    $envContent | Set-Content ".\env"
} else {
    Write-Host "[4/7] .env already exists, skipping." -ForegroundColor Gray
}

Write-Host "`nCurrent .env contents:" -ForegroundColor DarkCyan
if (Test-Path ".\env") {
    Get-Content ".\env"
} else {
    Write-Host ".env file not found" -ForegroundColor Red
}
Write-Host "------`n"

# 5. Database migrate
Write-Host "[5/7] Migrating database (SQLite by default)..." -ForegroundColor Yellow
$pythonExe = ".venv\Scripts\python.exe"
& $pythonExe manage.py migrate

# 6. Seed admin account
Write-Host "[6/7] Seeding default admin user..." -ForegroundColor Yellow
& $pythonExe manage.py seed

# 6b. Optional: Seed dummy data
Write-Host "[6b/7] Would you like to populate with dummy data? (Y/N)" -ForegroundColor Cyan
$seedDummy = Read-Host
if ($seedDummy -eq "Y" -or $seedDummy -eq "y") {
    Write-Host "Seeding comprehensive dummy data..." -ForegroundColor Yellow
    & $pythonExe manage.py seed_data
} else {
    Write-Host "Skipping dummy data seeding." -ForegroundColor Gray
}

# 7. Launch dev server
Write-Host "[7/7] Starting Django dev server on http://127.0.0.1:8000 ..." -ForegroundColor Green
& $pythonExe manage.py runserver
