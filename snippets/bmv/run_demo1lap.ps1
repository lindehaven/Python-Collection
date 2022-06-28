# Run OBC system demo
# Author : Lars Lindehaven
# Date   : 2019-06-12

if ($Args.Length -gt 0) {
    $Wait = $Args[0]
} else {
    $Wait = 0.0
}

del -EA SilentlyContinue .\obccu.p
del -EA SilentlyContinue .\obceu.p

"`r`nRunning system demo part 1 'First lap ever, 40 seconds, charged to 3%'. Please wait..."
Get-Content .\testlap1.dat | python.exe .\obcwu.py --wait $Wait --charge 3.0
""

