import re
print("starting")
file_object = open("testOutput.txt", "r")
x= re.findall("Failed: .", file_object.read())
if(len(x) >0):
    failedTests = x[0][8:]
    print(failedTests)
