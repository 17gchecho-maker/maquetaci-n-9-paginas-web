$ErrorActionPreference = "Stop"

# Rename index1.html and index1.js if they exist
if (Test-Path "index1.html") {
    Rename-Item -Path "index1.html" -NewName "index.html" -Force
    Write-Host "Renamed index1.html to index.html"
}
if (Test-Path "index1.js") {
    Rename-Item -Path "index1.js" -NewName "index.js" -Force
}

# Process all HTML files
Get-ChildItem -Filter "*.html" | ForEach-Object {
    $filepath = $_.FullName
    $filename = $_.Name
    Write-Host "Processing $filename"
    
    $content = Get-Content $filepath -Raw
    
    # 1. Replace index1.html with index.html
    $content = $content -replace 'href="index1.html"', 'href="index.html"'
    
    # 2. Fix navbar active states
    # Remove all active classes
    $content = $content -replace 'class="nav-link active"', 'class="nav-link"'
    $content = $content -replace '\s*aria-current="page"', ''
    
    # Add active class back to the current page
    # Look for: class="nav-link" href="filename"
    $targetName = [regex]::Escape($filename)
    $pattern = 'class="nav-link"\s*href="' + $targetName + '"'
    $replacement = 'class="nav-link active" aria-current="page" href="' + $filename + '"'
    
    # Also look for cases with extra spaces
    $pattern2 = '(class="nav-link")(\s+)(href="' + $targetName + '")'
    $replacement2 = '$1 active" aria-current="page" $3'
    
    $content = $content -replace $pattern, $replacement
    $content = $content -replace $pattern2, $replacement2
    
    Set-Content -Path $filepath -Value $content -Encoding UTF8
}

Write-Host "Done fixing HTML links."
