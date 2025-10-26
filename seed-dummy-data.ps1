<#
.SYNOPSIS
    Seeds the NHS Service Tracker database with comprehensive dummy data.
.DESCRIPTION
    Populates the database with realistic patient records, NHS services, 
    and appointment data spanning 90 days for testing and demonstration.
#>

Write-Host "=== NHS Service Tracker: Dummy Data Seeding ===" -ForegroundColor Cyan

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.venv\Scripts\Activate.ps1

# Seed comprehensive dummy data
Write-Host "Populating database with dummy data..." -ForegroundColor Yellow
.venv\Scripts\python.exe -m flask --app manage seed-data

Write-Host "`n✅ Dummy data seeding completed!" -ForegroundColor Green
Write-Host "Your NHS Service Tracker now contains:" -ForegroundColor Cyan
Write-Host "  • 12 NHS Services (GP, Cardiology, Mental Health, etc.)" -ForegroundColor White
Write-Host "  • 15 Patient Records (with realistic NHS numbers)" -ForegroundColor White  
Write-Host "  • 200+ Appointments (past, present, and future)" -ForegroundColor White
Write-Host "`nYou can now test the full functionality of your application!" -ForegroundColor Green