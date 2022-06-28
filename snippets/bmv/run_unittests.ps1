# Run OBC unit tests
# Author : Lars Lindehaven
# Date   : 2019-06-05

# TODO: Remove all persistent data
del -EA SilentlyContinue .\obccu.p
del -EA SilentlyContinue .\obceu.p

# OBC Control Unit

"`r`n-------- test_obccu.TestSuiteBasic --------`r`n"
python -m unittest test_obccu.TestSuiteBasic

"`r`n-------- test_obccu.TestSuiteTough --------`r`n"
python -m unittest test_obccu.TestSuiteTough


# OBC Energy Unit

"`r`n-------- test_obceu.TestSuiteBasic --------`r`n"
python -m unittest test_obceu.TestSuiteBasic

""
