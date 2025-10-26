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

# 4. Create .env with secure key
if (!(Test-Path ".\env")) {
    Write-Host "[4/7] Creating .env file with secure SECRET_KEY..." -ForegroundColor Yellow
    
    # Generate secure secret key using Python
    $secret = python -c "import secrets; print(secrets.token_hex(32))"
    
    # Create .env file with default configuration
    $envContent = @"
FLASK_APP=wsgi.py
FLASK_ENV=development
FLASK_DEBUG=1
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

# 5. Database init + migrate + upgrade
Write-Host "[5/7] Initialising / migrating database (SQLite by default)..." -ForegroundColor Yellow
$pythonExe = ".venv\Scripts\python.exe"
try {
    & $pythonExe -m flask --app wsgi db init
} catch {
    Write-Host "Migrations folder already exists." -ForegroundColor Gray
}
try {
    & $pythonExe -m flask --app wsgi db migrate -m "init"
} catch {
    Write-Host "Migration already exists." -ForegroundColor Gray
}
& $pythonExe -m flask --app wsgi db upgrade

# 6. Seed roles + admin account
Write-Host "[6/7] Seeding roles and default admin user..." -ForegroundColor Yellow
& $pythonExe -m flask --app manage seed

# 6b. Optional: Seed dummy data
Write-Host "[6b/7] Would you like to populate with dummy data? (Y/N)" -ForegroundColor Cyan
$seedDummy = Read-Host
if ($seedDummy -eq "Y" -or $seedDummy -eq "y") {
    Write-Host "Seeding comprehensive dummy data..." -ForegroundColor Yellow
    & $pythonExe -m flask --app manage seed-data
} else {
    Write-Host "Skipping dummy data seeding." -ForegroundColor Gray
}

# 7. Launch dev server
Write-Host "[7/7] Starting Flask dev server on http://127.0.0.1:5000 ..." -ForegroundColor Green
& $pythonExe -m flask --app wsgi run
