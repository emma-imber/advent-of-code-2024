import ast

data = open('input.txt').read()
entries = data.split("\n")

# part 1

turningPoints = []
wholeMap = []
currentStatus = [[], 'up']

for yCoord, line in enumerate(entries):
    for xCoord, char in enumerate(line):
        wholeMap.append([xCoord, yCoord])
        if char == '#':
            turningPoints.append([xCoord, yCoord])
        elif char == '^':
            currentStatus[0] = [xCoord, yCoord]

startingStatus = currentStatus.copy()

def walk(position):
    position = currentStatus[0]
    direction = currentStatus[1]
    nextPos = position.copy()
    if direction == 'up':
        nextPos[1] -= 1
        if nextPos in turningPoints:
            return [position, 'right']
        else:
            return [nextPos, direction]
    elif direction == 'right':
        nextPos[0] += 1
        if nextPos in turningPoints:
            return [position, 'down']
        else:
            return [nextPos, direction]
    elif direction == 'down':
        nextPos[1] += 1
        if nextPos in turningPoints:
            return [position, 'left']
        else:
            return [nextPos, direction]
    elif direction == 'left':
        nextPos[0] -= 1
        if nextPos in turningPoints:
            return [position, 'up']
        else:
            return [nextPos, direction]

walking = True
visitedPositions = {str(currentStatus[0].copy())}

while walking:
    currentStatus = walk(currentStatus)
    visitedPositions.add(str(currentStatus[0].copy()))
    if currentStatus[0] not in wholeMap:
        walking = False

print(len(visitedPositions) - 1)

# part 2
# brute force over anything in visitedPositions since it can only be where the guard walks
# very slow but it works

loopablePositions = 0
newVisitedPositions = {str(currentStatus[0].copy())}

for position in visitedPositions:
    print(position)
    turningPoints.append(ast.literal_eval(position))
    currentStatus = startingStatus
    isLoop = True
    newVisitedPositions = {str(currentStatus[0].copy())}
    walkCounter = 0

    # 25000 is kind of arbitrary, just seemed like roughly the right limit to use
    while walkCounter < 25000:
        currentStatus = walk(currentStatus)
        walkCounter += 1
        if currentStatus[0] not in wholeMap:
            isLoop = False
            break
        if str(currentStatus) in newVisitedPositions:
            break
        newVisitedPositions.add(str(currentStatus.copy()))

    if isLoop:
        loopablePositions += 1

    turningPoints.pop()

print(loopablePositions)