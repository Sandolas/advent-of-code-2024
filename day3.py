import re
import sys

def main():
    mulExpressionList = []
    with open(sys.argv[1]) as inputfile:
        inputString = inputfile.read()

    mulPattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    enableString  = "do()"
    disableString = "don't()"

    enablePattern  = re.escape(enableString)
    disablePattern = re.escape(disableString)
    validExpressionPattern = f"{mulPattern}|{enablePattern}|{disablePattern}"
    mulExpressionList += re.findall(validExpressionPattern, inputString)

    multiplicationSum = 0
    currentlyEnabled = True
    for expression in mulExpressionList:
        if expression == enableString:
            currentlyEnabled = True
        elif expression == disableString:
            currentlyEnabled = False
        else:
            # multiplication expression
            if currentlyEnabled:
                multiplicationSum += evaluate(expression)

    print(f"Sum of all multiplication instructions: {multiplicationSum}")

def evaluate(expression):
    numberStrings = re.findall(r"[0-9]+", expression)
    a = int(numberStrings[0])
    b = int(numberStrings[1])

    return a * b

main()
