# Save this script as check-status-all-branches.ps1

# Fetch all branches
git fetch --all

# Get a list of all remote branches
$branches = git branch -r | Where-Object { $_ -notmatch '->' }

# Loop through each branch
foreach ($branch in $branches) {
    # Extract the branch name
    $branchName = $branch -replace 'origin/', ''

    # Checkout the branch
    git checkout $branchName

    # Check the status
    Write-Output "Status of branch ${branchName}:"
    git status
}

# Checkout back to the main branch (or any branch you prefer)
git checkout main