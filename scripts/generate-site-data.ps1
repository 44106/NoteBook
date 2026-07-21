param(
  [string]$OutputPath = (Join-Path $PSScriptRoot "..\site-data.js")
)

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$knowledgeRoots = @("大二春夏", "大二秋冬")

$resources = foreach ($semester in $knowledgeRoots) {
  $semesterPath = Join-Path $repositoryRoot $semester
  if (-not (Test-Path -LiteralPath $semesterPath)) {
    continue
  }

  Get-ChildItem -LiteralPath $semesterPath -File -Recurse | ForEach-Object {
    $relativePath = $_.FullName.Substring($repositoryRoot.Length + 1).Replace("\", "/")
    $pathParts = $relativePath.Split("/")
    $extension = $_.Extension.TrimStart(".").ToLowerInvariant()

    [ordered]@{
      title = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
      fileName = $_.Name
      path = $relativePath
      semester = $pathParts[0]
      course = if ($pathParts.Length -gt 1) { $pathParts[1] } else { "未分类" }
      type = if ($extension) { $extension } else { "file" }
      size = $_.Length
      modified = $_.LastWriteTime.ToString("yyyy-MM-dd")
    }
  }
}

$json = @($resources) | ConvertTo-Json -Depth 3
[System.IO.File]::WriteAllText(
  (Resolve-Path -LiteralPath $OutputPath),
  "window.SITE_RESOURCES = $json;`r`n",
  [System.Text.UTF8Encoding]::new($false)
)

Write-Output "Generated $(@($resources).Count) knowledge-base entries in $OutputPath"
