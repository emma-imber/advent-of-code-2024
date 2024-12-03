import re

data = open('input.txt', 'r').read().replace('\n', '')

# part 1

matches = re.findall("mul\(\d{1,10},\d{1,10}\)", data)

total = 0

for match in matches:
    numbersToMultiply = match[4:-1].split(',')
    total += int(numbersToMultiply[0]) * int(numbersToMultiply[1])

print(total)

# part 2

p2total = 0

doSections = data.split('do()')
for section in doSections:
    dontSections = section.split("don't()")
    sectionMatches = re.findall("mul\(\d{1,10},\d{1,10}\)", dontSections[0])
    for match in sectionMatches:
        numbersToMultiply = match[4:-1].split(',')
        p2total += int(numbersToMultiply[0]) * int(numbersToMultiply[1])

print(p2total)