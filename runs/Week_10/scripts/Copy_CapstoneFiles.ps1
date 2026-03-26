
<# 
.SYNOPSIS
  Copies new_inputs.npy from previous capstone run folders into this repo's Capstone\Week_XX structure,
  renaming them to initial_inputs.npy. Also copies Capstone_Strategy_Summary.docx into the Week_XX folder.

.PARAMETER week_num
  Week number (integer). Used to create Capstone\Week_XX destination folder. Default = 3

.PARAMETER prev_FilePath
  Source root path that contains function_1 .. function_8 folders and Capstone_Strategy_Summary.docx.
  Default = "C:\Users\AntoniusMeliat\source\Python\JupyterNotebooks\13.1\Capstone"

.NOTES
  Destination base is relative to script location: $PSScriptRoot\Capstone\Week_XX
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [ValidateRange(1, 99)]
    [int]$week_num = 10,

    [Parameter(Mandatory = $false)]
    [string]$prev_FilePath = "C:\Users\AntoniusMeliat\source\Python\JupyterNotebooks\20.1\Capstone"
)

# Fail early on common issues
Set-StrictMode -Version Latest

# Resolve destination base: <script dir>\Capstone\Week_XX
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$destCapstoneRoot = Join-Path $scriptDir 'Capstone'
#$destWeekFolder   = Join-Path $destCapstoneRoot
Write-Host $destWeekFolder


# Ensure destination week folder exists
if (-not (Test-Path -Path $destCapstoneRoot)) {
    New-Item -Path $destCapstoneRoot -ItemType Directory -Force | Out-Null
}

Write-Host ("Destination week folder: {0}" -f $destCapstoneRoot) -ForegroundColor Cyan
Write-Host ("Source base folder     : {0}" -f $prev_FilePath)   -ForegroundColor Cyan

# Validate source base
if (-not (Test-Path -Path $prev_FilePath)) {
    Write-Error ("Source base path not found: {0}" -f $prev_FilePath)
    exit 1
}

# Loop through function_1 .. function_8
for ($folder_counter = 1; $folder_counter -le 8; $folder_counter++) {

    $current_folder = "function_{0}" -f $folder_counter
    $srcFolder = Join-Path $prev_FilePath $current_folder
 

    $srcNewInputs  = Join-Path $srcFolder "new_inputs.npy"
    $srcNewOutputs = Join-Path $srcFolder "new_outputs.npy"

    $destFunctionFolder = Join-Path $destCapstoneRoot $current_folder
    $destInitInputs     = Join-Path $destFunctionFolder "initial_inputs.npy"
    $destInitOutputs    = Join-Path $destFunctionFolder "initial_outputs.npy"

    # Ensure destination function folder exists
    if (-not (Test-Path -Path $destFunctionFolder)) {
        New-Item -Path $destFunctionFolder -ItemType Directory -Force | Out-Null
        Write-Host ("Created destination folder: {0}" -f $destFunctionFolder) -ForegroundColor Yellow
    }

    # Copy new_inputs.npy -> initial_inputs.npy
    if (Test-Path -Path $srcNewInputs) {
        try {
            Copy-Item -Path $srcNewInputs -Destination $destInitInputs -Force
            Write-Host ("Copied {0}: new_inputs.npy -> initial_inputs.npy" -f $current_folder) -ForegroundColor Green
        }
        catch {
            Write-Warning ("Failed to copy inputs for {0}. Error: {1}" -f $current_folder, $_.Exception.Message)
        }
    }
    else {
        Write-Warning ("Source inputs not found for {0}: {1}" -f $current_folder, $srcNewInputs)
    }

    # Copy new_outputs.npy -> initial_outputs.npy
    if (Test-Path -Path $srcNewOutputs) {
        try {
            Copy-Item -Path $srcNewOutputs -Destination $destInitOutputs -Force
            Write-Host ("Copied {0}: new_outputs.npy -> initial_outputs.npy" -f $current_folder) -ForegroundColor Green
        }
        catch {
            Write-Warning ("Failed to copy outputs for {0}. Error: {1}" -f $current_folder, $_.Exception.Message)
        }
    }
    else {
        Write-Warning ("Source outputs not found for {0}: {1}" -f $current_folder, $srcNewOutputs)
    }
}

# Copy Capstone_Strategy_Summary.docx to the week folder
$summaryName = "Capstone Strategy.ipynb"
$srcSummary  = Join-Path $prev_FilePath $summaryName
$destSummary = Join-Path $destCapstoneRoot $summaryName

if (Test-Path -Path $srcSummary) {
    try {
        Copy-Item -Path $srcSummary -Destination $destSummary -Force
        Write-Host ("Copied summary: {0} -> {1}" -f $summaryName, $destCapstoneRoot) -ForegroundColor Green
    }
    catch {
        Write-Warning ("Failed to copy summary. Error: {0}" -f $_.Exception.Message)
    }
}
else {
    Write-Warning ("Summary not found: {0}" -f $srcSummary)
}

Write-Host "Done." -ForegroundColor Cyan