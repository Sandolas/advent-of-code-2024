import re
import sys

def main():
    enableString  = "do()"
    disableString = "don't()"
    mulPattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    expressionList = []
    enablePattern  = re.escape(enableString)
    disablePattern = re.escape(disableString)
    validExpressionPattern = f"{mulPattern}|{enablePattern}|{disablePattern}"

    with open(sys.argv[1]) as inputfile:
        inputString = inputfile.read()

    expressionList += re.findall(validExpressionPattern, inputString)

    multiplicationSum = 0
    currentlyEnabled = True
    for expression in expressionList:
        if expression == enableString:
            currentlyEnabled = True
        elif expression == disableString:
            currentlyEnabled = False
        else:
            # multiplication expression
            if currentlyEnabled:
                multiplicationSum += evaluate(expression)

    # TODO: Restore part 1 solution calculation
    print(f"Sum of all multiplication instructions: {multiplicationSum}")

def evaluate(expression):
    numberStrings = re.findall(r"[0-9]+", expression)
    a = int(numberStrings[0])
    b = int(numberStrings[1])

    return a * b

main()
