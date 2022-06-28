# Create OBC documentation
# Author :  Lars Lindehaven
# Date   :  2019-05-15

del obc*.html
python -m pydoc -w obccu
python -m pydoc -w obcdu
python -m pydoc -w obceu
python -m pydoc -w obceu_stub
python -m pydoc -w obcwu

# Compress archive
# 7z.exe a -tzip obcdoc.zip obc*.html
