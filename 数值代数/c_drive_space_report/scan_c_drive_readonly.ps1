$ErrorActionPreference = 'Continue'

$ReportDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = 'C:\'
$TopN = 300
$LargeFileThresholdBytes = 100MB
$ProgressPath = Join-Path $ReportDir 'progress.txt'
$SummaryPath = Join-Path $ReportDir 'scan_summary.json'
$LargeFilesPath = Join-Path $ReportDir 'large_files_over_100MB.csv'
$TopFilesPath = Join-Path $ReportDir 'largest_files_top300.csv'
$DirSummaryPath = Join-Path $ReportDir 'directory_size_summary.csv'
$ExtensionPath = Join-Path $ReportDir 'size_by_extension_top100.csv'
$ReportPath = Join-Path $ReportDir 'README_C_drive_space_report.md'
$ErrorSamplePath = Join-Path $ReportDir 'scan_errors_sample.txt'

function Format-Bytes {
    param([double]$Bytes)
    if ($Bytes -ge 1TB) { return ('{0:N2} TB' -f ($Bytes / 1TB)) }
    if ($Bytes -ge 1GB) { return ('{0:N2} GB' -f ($Bytes / 1GB)) }
    if ($Bytes -ge 1MB) { return ('{0:N2} MB' -f ($Bytes / 1MB)) }
    if ($Bytes -ge 1KB) { return ('{0:N2} KB' -f ($Bytes / 1KB)) }
    return ('{0:N0} B' -f $Bytes)
}

function Add-Size {
    param(
        [hashtable]$Table,
        [string]$Key,
        [long]$Bytes
    )
    if ([string]::IsNullOrWhiteSpace($Key)) { return }
    if ($Table.ContainsKey($Key)) {
        $Table[$Key] += $Bytes
    } else {
        $Table[$Key] = [int64]$Bytes
    }
}

function Convert-ToSizeRows {
    param([hashtable]$Table, [int]$First = 200)
    $Table.GetEnumerator() |
        Sort-Object Value -Descending |
        Select-Object -First $First |
        ForEach-Object {
            [pscustomobject]@{
                PathOrKey = $_.Key
                SizeBytes = [int64]$_.Value
                SizeGB    = [math]::Round($_.Value / 1GB, 3)
                Size      = Format-Bytes $_.Value
            }
        }
}

function Get-PathParts {
    param([string]$Path)
    $trimmed = $Path
    if ($trimmed.StartsWith('C:\', [StringComparison]::OrdinalIgnoreCase)) {
        $trimmed = $trimmed.Substring(3)
    }
    if ([string]::IsNullOrWhiteSpace($trimmed)) { return @() }
    return $trimmed.Split([char[]]@('\'), [System.StringSplitOptions]::RemoveEmptyEntries)
}

function Get-PrefixPath {
    param([string[]]$Parts, [int]$Depth)
    if ($Parts.Count -lt $Depth) { return $null }
    return 'C:\' + (($Parts[0..($Depth - 1)]) -join '\')
}

function Get-AnchorChild {
    param([string]$Path, [string]$Anchor)
    if (-not $Path.StartsWith($Anchor, [StringComparison]::OrdinalIgnoreCase)) { return $null }
    $rest = $Path.Substring($Anchor.Length).TrimStart('\')
    if ([string]::IsNullOrWhiteSpace($rest)) { return $Anchor }
    $first = $rest.Split([char[]]@('\'), 2, [System.StringSplitOptions]::RemoveEmptyEntries)[0]
    return (Join-Path $Anchor $first)
}

function Add-FileRecord {
    param(
        [string]$Path,
        [long]$Length,
        [datetime]$LastWriteTime
    )
    $script:TotalBytes += $Length
    $script:FileCount += 1

    $ext = [System.IO.Path]::GetExtension($Path)
    if ([string]::IsNullOrWhiteSpace($ext)) { $ext = '[no extension]' }
    Add-Size $script:ExtTotals $ext.ToLowerInvariant() $Length

    $parts = Get-PathParts $Path
    foreach ($depth in 1..4) {
        $prefix = Get-PrefixPath $parts $depth
        if ($null -ne $prefix) { Add-Size $script:DirDepthTotals $prefix $Length }
    }

    foreach ($anchor in $script:AnchorPaths) {
        $child = Get-AnchorChild $Path $anchor
        if ($null -ne $child) { Add-Size $script:AnchorChildTotals $child $Length }
    }

    if ($Length -ge $script:LargeFileThresholdBytes) {
        $script:LargeFiles.Add([pscustomobject]@{
            Path          = $Path
            SizeBytes     = [int64]$Length
            SizeGB        = [math]::Round($Length / 1GB, 3)
            Size          = Format-Bytes $Length
            Extension     = $ext.ToLowerInvariant()
            LastWriteTime = $LastWriteTime
        }) | Out-Null
    }
}

function Write-ProgressFile {
    $elapsed = (Get-Date) - $script:StartTime
    $drive = Get-PSDrive -Name C
    $lines = @(
        "Status: running",
        "Started: $($script:StartTime.ToString('yyyy-MM-dd HH:mm:ss'))",
        "Now: $((Get-Date).ToString('yyyy-MM-dd HH:mm:ss'))",
        "Elapsed: $([math]::Round($elapsed.TotalMinutes, 2)) minutes",
        "Files scanned: $script:FileCount",
        "Directories scanned: $script:DirectoryCount",
        "Bytes accounted from readable files: $(Format-Bytes $script:TotalBytes)",
        "Skipped reparse points: $script:ReparseSkipped",
        "Access/read errors: $script:ErrorCount",
        "Current free space on C: $(Format-Bytes $drive.Free)"
    )
    Set-Content -LiteralPath $script:ProgressPath -Value $lines -Encoding UTF8
}

$StartTime = Get-Date
$TotalBytes = [int64]0
$FileCount = [int64]0
$DirectoryCount = [int64]0
$ErrorCount = [int64]0
$ReparseSkipped = [int64]0
$LastProgressWrite = Get-Date
$LargeFiles = New-Object System.Collections.Generic.List[object]
$ExtTotals = @{}
$DirDepthTotals = @{}
$AnchorChildTotals = @{}
$ErrorSamples = New-Object System.Collections.Generic.List[string]

$AnchorPaths = @(
    'C:\Users\njb18',
    'C:\Users\njb18\Downloads',
    'C:\Users\njb18\Desktop',
    'C:\Users\njb18\Documents',
    'C:\Users\njb18\AppData',
    'C:\Users\njb18\AppData\Local',
    'C:\Users\njb18\AppData\Roaming',
    'C:\Users\njb18\.cache',
    'C:\Users\njb18\.conda',
    'C:\Users\njb18\.codex',
    'C:\ProgramData',
    'C:\Program Files',
    'C:\Program Files (x86)',
    'C:\Windows',
    'C:\$Recycle.Bin'
) | Where-Object { Test-Path -LiteralPath $_ }

Write-ProgressFile

$stack = New-Object System.Collections.Generic.Stack[string]
$stack.Push($Root)

while ($stack.Count -gt 0) {
    $dir = $stack.Pop()
    $DirectoryCount += 1

    try {
        $entries = [System.IO.Directory]::EnumerateFileSystemEntries($dir)
    } catch {
        $ErrorCount += 1
        if ($ErrorSamples.Count -lt 300) { $ErrorSamples.Add("DIR`t$dir`t$($_.Exception.Message)") | Out-Null }
        continue
    }

    foreach ($entry in $entries) {
        try {
            $attributes = [System.IO.File]::GetAttributes($entry)
        } catch {
            $ErrorCount += 1
            if ($ErrorSamples.Count -lt 300) { $ErrorSamples.Add("ATTR`t$entry`t$($_.Exception.Message)") | Out-Null }
            continue
        }

        if (($attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
            $ReparseSkipped += 1
            continue
        }

        if (($attributes -band [System.IO.FileAttributes]::Directory) -ne 0) {
            $stack.Push($entry)
            continue
        }

        try {
            $fileInfo = [System.IO.FileInfo]::new($entry)
            Add-FileRecord -Path $fileInfo.FullName -Length $fileInfo.Length -LastWriteTime $fileInfo.LastWriteTime
        } catch {
            $ErrorCount += 1
            if ($ErrorSamples.Count -lt 300) { $ErrorSamples.Add("FILE`t$entry`t$($_.Exception.Message)") | Out-Null }
        }
    }

    if (((Get-Date) - $LastProgressWrite).TotalSeconds -ge 10) {
        Write-ProgressFile
        $LastProgressWrite = Get-Date
    }
}

$FinishedTime = Get-Date
$largeSorted = $LargeFiles | Sort-Object SizeBytes -Descending
$topFiles = $largeSorted | Select-Object -First $TopN
$dirRows = @()
$dirRows += Convert-ToSizeRows $DirDepthTotals 300
$dirRows += Convert-ToSizeRows $AnchorChildTotals 300
$dirRows = $dirRows | Sort-Object SizeBytes -Descending | Select-Object -First 500
$extRows = Convert-ToSizeRows $ExtTotals 100

$largeSorted | Export-Csv -LiteralPath $LargeFilesPath -NoTypeInformation -Encoding UTF8
$topFiles | Export-Csv -LiteralPath $TopFilesPath -NoTypeInformation -Encoding UTF8
$dirRows | Export-Csv -LiteralPath $DirSummaryPath -NoTypeInformation -Encoding UTF8
$extRows | Export-Csv -LiteralPath $ExtensionPath -NoTypeInformation -Encoding UTF8
$ErrorSamples | Set-Content -LiteralPath $ErrorSamplePath -Encoding UTF8

$driveFinal = Get-PSDrive -Name C
$summary = [pscustomobject]@{
    status                 = 'completed'
    started                = $StartTime.ToString('yyyy-MM-dd HH:mm:ss')
    finished               = $FinishedTime.ToString('yyyy-MM-dd HH:mm:ss')
    elapsed_minutes        = [math]::Round((New-TimeSpan -Start $StartTime -End $FinishedTime).TotalMinutes, 2)
    files_scanned          = $FileCount
    directories_scanned    = $DirectoryCount
    readable_bytes         = $TotalBytes
    readable_size          = Format-Bytes $TotalBytes
    large_file_threshold   = Format-Bytes $LargeFileThresholdBytes
    large_files_found      = $LargeFiles.Count
    skipped_reparse_points = $ReparseSkipped
    access_or_read_errors  = $ErrorCount
    c_free_bytes_after     = [int64]$driveFinal.Free
    c_free_after           = Format-Bytes $driveFinal.Free
}
$summary | ConvertTo-Json | Set-Content -LiteralPath $SummaryPath -Encoding UTF8

$topFileLines = $topFiles | Select-Object -First 30 | ForEach-Object {
    "| $($_.Size) | `$($_.Path)` | $($_.LastWriteTime) |"
}
$topDirLines = $dirRows | Select-Object -First 40 | ForEach-Object {
    "| $($_.Size) | `$($_.PathOrKey)` |"
}
$topExtLines = $extRows | Select-Object -First 30 | ForEach-Object {
    "| $($_.Size) | `$($_.PathOrKey)` |"
}

$report = @"
# C Drive Space Report

Generated: $($FinishedTime.ToString('yyyy-MM-dd HH:mm:ss'))

This scan was read-only. It did not delete, move, rename, or modify C drive files. It skipped reparse points to avoid following junctions/symlinks.

## Summary

- C drive free space after scan: $(Format-Bytes $driveFinal.Free)
- Readable file bytes accounted: $(Format-Bytes $TotalBytes)
- Files scanned: $FileCount
- Directories scanned: $DirectoryCount
- Files >= $(Format-Bytes $LargeFileThresholdBytes): $($LargeFiles.Count)
- Skipped reparse points: $ReparseSkipped
- Access/read errors: $ErrorCount

## Largest Files

Full CSV: `largest_files_top300.csv`

| Size | Path | Last modified |
| ---: | --- | --- |
$($topFileLines -join "`r`n")

## Largest Directory Buckets

Full CSV: `directory_size_summary.csv`

| Size | Path |
| ---: | --- |
$($topDirLines -join "`r`n")

## Largest Extension Groups

Full CSV: `size_by_extension_top100.csv`

| Size | Extension |
| ---: | --- |
$($topExtLines -join "`r`n")

## Notes

- Treat this as a triage list, not a delete list.
- Prefer uninstallers for applications, virtual machines, SDKs, and package managers.
- Be careful with `C:\Windows`, `C:\Program Files`, `C:\ProgramData`, user profile databases, `.git` directories, and WSL/VM disk images.
- Archives, installers, ISO files, duplicate datasets, old model checkpoints, build folders, caches, and temporary downloads are usually better review candidates.
"@
$report | Set-Content -LiteralPath $ReportPath -Encoding UTF8

$doneLines = @(
    "Status: completed",
    "Started: $($StartTime.ToString('yyyy-MM-dd HH:mm:ss'))",
    "Finished: $($FinishedTime.ToString('yyyy-MM-dd HH:mm:ss'))",
    "Elapsed: $([math]::Round((New-TimeSpan -Start $StartTime -End $FinishedTime).TotalMinutes, 2)) minutes",
    "Files scanned: $FileCount",
    "Directories scanned: $DirectoryCount",
    "Bytes accounted from readable files: $(Format-Bytes $TotalBytes)",
    "Files >= $(Format-Bytes $LargeFileThresholdBytes): $($LargeFiles.Count)",
    "Skipped reparse points: $ReparseSkipped",
    "Access/read errors: $ErrorCount",
    "Current free space on C: $(Format-Bytes $driveFinal.Free)",
    "Report: $ReportPath"
)
Set-Content -LiteralPath $ProgressPath -Value $doneLines -Encoding UTF8
