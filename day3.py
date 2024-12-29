import re
import sys

def main():
    mulExpressionList = []
    with open(sys.argv[1]) as inputfile:
        for line in inputfile:
            pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
            mulExpressionList += re.findall(pattern, line)

    multiplicationSum = 0
    for expression in mulExpressionList:
        multiplicationSum += evaluate(expression)

    print(f"Sum of all multiplication instructions: {multiplicationSum}")

def evaluate(expression):
    numberStrings = re.findall(r"[0-9]+", expression)
    a = int(numberStrings[0])
    b = int(numberStrings[1])

    return a * b

main()
