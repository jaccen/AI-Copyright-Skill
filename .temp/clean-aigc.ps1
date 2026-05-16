# clean-aigc.ps1 v3
# AIGC水印清理脚本：清理YAML frontmatter中的AIGC块 + 正文内联AIGC注入 + 孤立`---` + 文末`> AI生成`标记
# 智能区分AIGC字段与合法YAML字段（name/version/author/tags/trigger等），只删前者

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $repoRoot

$files = @(
    "SKILL.md",
    "README.md",
    "README_CN.md",
    "references\ai-patent-special.md",
    "references\ai-patent-claims-guide.md",
    "references\ai-software-copyright-guide.md"
)

$cleaned = 0

foreach ($f in $files) {
    $path = Join-Path $repoRoot $f
    if (-not (Test-Path $path)) { continue }
    
    $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
    $original = $content
    
    # 1. 清理YAML frontmatter中的AIGC字段块（多行，ContentProducer到ReservedCode2）
    $content = $content -replace '(?m)^  ContentProducer:.*\r?\n  ContentPropagator:.*\r?\n  Label:.*\r?\n  ProduceID:.*\r?\n  PropagateID:.*\r?\n  ReservedCode1:.*\r?\n  ReservedCode2:.*\r?\n', ''
    
    # 2. 清理正文中联AIGC注入块
    $content = $content -replace '(?s)---\s*\r?\nAIGC:.*?---\s*\r?\n', ''
    
    # 3. 清理文末 `> AI生成` 标记
    $content = $content -replace '(?m)^\s*> AI生成\s*$', ''
    
    # 4. 清理孤立`---`（仅当其前后有空行且不在YAML frontmatter中）
    # 注意：SKILL.md的合法YAML frontmatter以---开头和结尾，不能删
    
    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($path, $content, (New-Object System.Text.UTF8Encoding $false))
        $cleaned++
        Write-Host "CLEANED: $f"
    } else {
        Write-Host "OK: $f"
    }
}

Write-Host ""
Write-Host "Total cleaned: $cleaned file(s)"
