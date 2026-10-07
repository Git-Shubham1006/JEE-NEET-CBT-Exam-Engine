# =============================================================================
# Automated Daily Git Push Script — RannVijay JEE/NEET CBT Platform
# Runs daily at 11:00 PM Sharp (23:00 IST)
# =============================================================================

$repoPath = "D:\AGENT\06-JEE-CBT-Platform"
$logPath = "$repoPath\auto-sync.log"
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Add-Content -Path $logPath -Value "[$timestamp] --- Running Daily 11:00 PM Git Sync ---"

if (-not (Test-Path $repoPath)) {
    Add-Content -Path $logPath -Value "[$timestamp] Error: Repository directory not found at $repoPath"
    exit 1
}

Set-Location $repoPath

try {
    # Check if there are changes
    $status = git status --porcelain
    if ($status) {
        Add-Content -Path $logPath -Value "[$timestamp] Detected uncommitted changes. Staging and committing..."
        git add .
        git commit -m "chore(daily-sync): automated 11:00 PM sync on $timestamp"
        $pushResult = git push origin main 2>&1
        Add-Content -Path $logPath -Value "[$timestamp] Push successfully completed: $pushResult"
    } else {
        # Check if local is ahead of remote
        $ahead = git status -sb
        if ($ahead -match "ahead") {
            Add-Content -Path $logPath -Value "[$timestamp] Local branch ahead of remote. Pushing..."
            $pushResult = git push origin main 2>&1
            Add-Content -Path $logPath -Value "[$timestamp] Push result: $pushResult"
        } else {
            Add-Content -Path $logPath -Value "[$timestamp] Working tree is completely clean and up-to-date. Nothing to push."
        }
    }
} catch {
    Add-Content -Path $logPath -Value "[$timestamp] Error during git sync: $_"
}
