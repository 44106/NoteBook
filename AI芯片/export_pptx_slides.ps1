param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$OutputDir
)

$ErrorActionPreference = "Stop"
$fullInput = (Resolve-Path -LiteralPath $InputPath).Path
$fullOutput = Join-Path (Get-Location).Path $OutputDir
New-Item -ItemType Directory -Force -Path $fullOutput | Out-Null

$powerPoint = New-Object -ComObject PowerPoint.Application
$presentation = $null
try {
    $presentation = $powerPoint.Presentations.Open($fullInput, $true, $false, $false)
    for ($i = 1; $i -le $presentation.Slides.Count; $i++) {
        $target = Join-Path $fullOutput ("slide-{0:D3}.png" -f $i)
        $presentation.Slides.Item($i).Export($target, "PNG", 1600, 900)
    }
    Write-Output ("Exported {0} slides to {1}" -f $presentation.Slides.Count, $fullOutput)
}
finally {
    if ($presentation -ne $null) {
        $presentation.Close()
    }
    $powerPoint.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
}
