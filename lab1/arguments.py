import sys

array = []
for i in range(1,len(sys.argv)):
    if len(sys.argv[i]) >= 3:
        array.insert(0, sys.argv[i])

resultString = ""
for string in array:
    resultString += string + " "

print(resultString)