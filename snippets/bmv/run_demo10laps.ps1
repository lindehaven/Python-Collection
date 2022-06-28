# Run OBC system demo
# Author : Lars Lindehaven
# Date   : 2019-06-12

if ($Args.Length -gt 0) {
    $Wait = $Args[0]
} else {
    $Wait = 0.0
}

"`r`nRunning system demo part 3 'Ten continuous laps, 5 minutes, no charging'. Please wait..."
Get-Content .\testlap10.dat | python.exe .\obcwu.py --wait $Wait
""

