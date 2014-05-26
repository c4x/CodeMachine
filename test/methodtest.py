import os
filePath = os.getcwd() + "/" +"test.java"
if os.path.exists(filePath):
    os.remove(filePath)
print(filePath)
