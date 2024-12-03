data = open('input.txt').read()
entries = data.split("\n")

def isRowSafe(nums):
    safe = True
    # handle increasing case
    if int(nums[1]) - int(nums[0]) >= 1 and int(nums[1]) - int(nums[0]) <= 3:
        for index, entry in enumerate(nums):
            if index == 0 or index == 1:
                continue
            elif (int(nums[index]) - int(nums[index-1]) >= 1) and (int(nums[index]) - int(nums[index-1]) <= 3):
                continue
            else:
                safe = False
                break
    # handle decreasing case
    elif int(nums[0]) - int(nums[1]) >= 1 and int(nums[0]) - int(nums[1]) <= 3:
        for index, entry in enumerate(nums):
            if index == 0 or index == 1:
                continue
            elif int(nums[index-1]) - int(nums[index]) >= 1 and int(nums[index-1]) - int(nums[index]) <= 3:
                continue
            else:
                safe = False
                break
    else:
        safe = False
    
    return safe

# part 1

p1SafeTotal = 0

for index, entry in enumerate(entries):
    row = entry.split(' ')
    p1Safe = isRowSafe(row)
    if p1Safe:
        p1SafeTotal += 1

print('Part 1: ' + str(p1SafeTotal))

# part 2

p2SafeTotal = 0

for index, entry in enumerate(entries):
    row = entry.split(' ')
    startsSafe = isRowSafe(row)

    if startsSafe:
        p2SafeTotal += 1
    if not startsSafe:
        for index, level in enumerate(row):
            dampenedRow = row.copy()
            del dampenedRow[index]
            if isRowSafe(dampenedRow):
                p2SafeTotal += 1
                break

print('Part 2: ' + str(p2SafeTotal))


# function to check if row is safe
# if row is unsafe, try removing levels to see if it makes row safe