import sys

firstNumber = sys.argv[1]
operator = sys.argv[2]
secondNumber = sys.argv[3]

if operator == "+":
    print(float(firstNumber) + float(secondNumber))
elif operator == "-":
    print(float(firstNumber) - float(secondNumber))
elif operator == "*":
    print(float(firstNumber) * float(secondNumber))
else:
    print("Podano bledny operator")