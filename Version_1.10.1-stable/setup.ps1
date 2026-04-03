param(
    [string]$rootPath
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($rootPath)) {
    $rootPath = Split-Path -Parent $MyInvocation.MyCommand.Path
}

$rootPath = $rootPath.Trim().Trim('"').TrimEnd('\')
$rootPath = [System.IO.Path]::GetFullPath($rootPath)

$targetPath = Join-Path $rootPath "termyx.bat"
if (-not (Test-Path $targetPath)) {
    throw "Could not find launcher at '$targetPath'."
}

$ws = New-Object -ComObject WScript.Shell
$desktopPath = $ws.SpecialFolders("Desktop")
if ([string]::IsNullOrWhiteSpace($desktopPath)) {
    $desktopPath = [Environment]::GetFolderPath("DesktopDirectory")
}

if (-not (Test-Path $desktopPath)) {
    throw "Desktop folder not found at '$desktopPath'."
}

$shortcutPath = Join-Path $desktopPath "Termyx.lnk"
$s = $ws.CreateShortcut($shortcutPath)
$s.TargetPath = $targetPath
$s.WorkingDirectory = $rootPath

$icoPath = Join-Path $rootPath "termyx.ico"
if (Test-Path $icoPath) {
    $s.IconLocation = $icoPath
}

$s.Save()
