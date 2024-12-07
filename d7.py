from itertools import product
data = open('input.txt').read()
entries = data.split("\n")

# for part 2 just added the |
operators = '*+|'
valueSum = 0

for entry in entries:
    testValue = int(entry.split(': ')[0])
    equationValues = entry.split(": ")[1].split(' ')
    possibleOperations = product(operators, repeat=(len(equationValues) - 1))
    testResultPossible = False;

    for combo in possibleOperations:
        runningTotal = int(equationValues[0])

        for index, operator in enumerate(combo):
            # just added this extra if statement for part 2
            if operator == '|':
                runningTotal = int(str(runningTotal) + equationValues[index+1])
            elif operator == '*':
                runningTotal = runningTotal * int(equationValues[index + 1])
            else:
                runningTotal += int(equationValues[index + 1])

        if runningTotal == testValue:
            testResultPossible = True
            break

    if testResultPossible:
        valueSum += testValue

print(valueSum)
