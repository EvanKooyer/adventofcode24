
testcombo = ['56208', '95668']


def sumpairs(pair):
    sortedpairs = []
    sums = []

    for item in pair:
        numlist = []

        for num in item:
            numlist.append(int(num))
        numlist.sort()
        sortedpairs.append(numlist)

    for a, b in zip(sortedpairs[0], sortedpairs[1]):
        if a > b:
            sums.append(a-b)
        else:
            sums.append(b-a)
    print([sortedpairs, sums, sum(sums)])
    return sum(sums)


def listgenerator(filepath):
    with open(filepath) as file:
        for line in file:
            yield line.strip().split('   ')


solutionlist = []

for row in listgenerator('distancevalues.txt'):
    print(row)
    solutionlist.append(sumpairs(row))

solution = sum(solutionlist)

print(solutionlist)
print(solution)
