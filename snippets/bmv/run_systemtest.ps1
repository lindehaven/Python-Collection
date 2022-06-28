# Run OBC system tests
# Author : Lars Lindehaven
# Date   : 2019-06-04

# Define functions
function Wait-For-Key {
    "`r`nPress any key to continue " | Write-Host -NoNewLine
    $HOST.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | OUT-NULL
    $HOST.UI.RawUI.Flushinputbuffer()
    "`r`n"
}

function Remove-Persistent-Data {
    # TODO: Remove all persistent data
    del -EA SilentlyContinue .\obccu.p
    del -EA SilentlyContinue .\obceu.p
}

# Get command line arguments
if ($Args.Length -gt 0) {
    $Wait = $Args[0]
    if ($Args.Length -gt 1) {
        $Key = $Args[1]
    } else {
        $Key = 0
    }
} else {
    $Wait = 0.0
}

# Run test cases

Remove-Persistent-Data

"`r`nRunning system test 01: '3 seconds parked'. Please wait..."
"`r`nDist 000000.0 km | Rem 000600.0 km | Cur 000 km/h | Avg 000 km/h | Pwr 00 kW | Skid False | Spin False | Time 00000003 s | Rem 200 kWh"
Get-Content .\test01.dat | python.exe .\obcwu.py --wait $Wait --charge 100.0
if ($Key -gt 0) { Wait-For-Key }
""

"`r`nRunning system test 02: '15 seconds drive forward'. Please wait..."
"`r`nDist 000000.3 km | Rem 000599.7 km | Cur 000 km/h | Avg 062 km/h | Pwr 21 kW | Skid False | Spin False | Time 00000018 s | Rem 200 kWh"
Get-Content .\test02.dat | python.exe .\obcwu.py --wait $Wait
if ($Key -gt 0) { Wait-For-Key }
""

"`r`nRunning system test 03: '3 minutes drive forward'. Please wait..."
"`r`nDist 000005.7 km | Rem 000594.1 km | Cur 108 km/h | Avg 103 km/h | Pwr 36 kW | Skid False | Spin False | Time 00000198 s | Rem 198 kWh"
Get-Content .\test03.dat | python.exe .\obcwu.py --wait $Wait
if ($Key -gt 0) { Wait-For-Key }
""

"`r`nRunning system test 04: '3 minutes drive backward'. Please wait..."
"`r`nDist 000011.0 km | Rem 000588.5 km | Cur 108 km/h | Avg 105 km/h | Pwr 37 kW | Skid False | Spin False | Time 00000378 s | Rem 196 kWh"
Get-Content .\test04.dat | python.exe .\obcwu.py --wait $Wait
if ($Key -gt 0) { Wait-For-Key }
""
