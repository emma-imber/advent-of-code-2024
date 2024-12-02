data = open('input.txt').read()
entries = data.split("\n")

leftIds = []
rightIds = []

for index, entry in enumerate(entries):
    locationIds = entry.split('   ')
    leftIds.append(int(locationIds[0]))
    rightIds.append(int(locationIds[1]))

leftIds.sort()
rightIds.sort()

totalDiff = 0

for index, id in enumerate(leftIds):
    totalDiff += abs(leftIds[index] - rightIds[index])

print("Part 1: " + str(totalDiff))

totalSimilarityScore = 0

for index, id in enumerate(leftIds):
    totalSimilarityScore += leftIds[index] * rightIds.count(leftIds[index])

print("Part 2: " + str(totalSimilarityScore))