import sys

def histogram(string):
    print(string)
    charInStringList = {'a': 0}
    for char in string:
        if charInStringList.get(char) == None:
            charInStringList[char] = 1
        else:
            charInStringList[char] += 1
    return charInStringList

print(histogram("Ala ma kota"))