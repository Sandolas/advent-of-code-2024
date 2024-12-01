import csv

leftList = []
rightList = []
with open("input.tmp") as inputfile:
    for line in inputfile:
       leftNumberStr, rightNumberStr = line.strip().split("   ")
       leftList.append(int(leftNumberStr))
       rightList.append(int(rightNumberStr))

leftList.sort()
rightList.sort()

differenceSum = 0
for (leftNumber, rightNumber) in zip(leftList, rightList):
    differenceSum += abs(leftNumber - rightNumber)

print(differenceSum)
