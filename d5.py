from operator import methodcaller
from functools import cmp_to_key

data = open('input.txt').read()
entries = data.split("\n\n")

pageOrderingRules = list(map(methodcaller("split", "|"), entries[0].split("\n")))
listOfPagelists = list(map(methodcaller("split", ","), entries[1].split("\n")))

# dictionary will list what pages should appear after a given page key
rulesDict = {}

for rule in pageOrderingRules:
    if rule[0] in rulesDict.keys():
        rulesDict[rule[0]].append(rule[1])
    else:
        rulesDict[rule[0]] = [rule[1]]

# custom sort function for part 2
def comparePages(page1, page2):
    if page2 in rulesDict.keys():
        if page1 in rulesDict[page2]:
            return 1
        else: return -1
    else:
        return -1


part1MiddlePageSum = 0
part2MiddlePageSum = 0

for pagelist in listOfPagelists:
    pagelistValid = True
    for index, page in enumerate(pagelist):
        if page in rulesDict.keys():
            for prevPage in pagelist[0:index]:
                # if a previous page is present in the dictionary entry it means
                # that page should appear after, so the page list is invalid
                if prevPage in rulesDict[page]:
                    pagelistValid = False
    if pagelistValid:
        part1MiddlePageSum += int(pagelist[int((len(pagelist) - 1) / 2)])
    else:
        pagelist.sort(key=cmp_to_key(comparePages))
        part2MiddlePageSum += int(pagelist[int((len(pagelist) - 1) / 2)])

print("Part 1: " + str(part1MiddlePageSum))
print("Part 2: " + str(part2MiddlePageSum))