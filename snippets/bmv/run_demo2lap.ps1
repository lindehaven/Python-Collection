# Run OBC system demo
# Author : Lars Lindehaven
# Date   : 2019-06-12

if ($Args.Length -gt 0) {
    $Wait = $Args[0]
} else {
    $Wait = 0.0
}

"`r`nRunning system demo part 2 'Second lap, 40 seconds, no charging'. Please wait..."
Get-Content .\testlap1.dat | python.exe .\obcwu.py --wait $Wait
""

