def getdatalists(filepath):
    with open(filepath) as file:
        leftrow = []
        rightrow = []
        for line in file:
            strings = line.strip().split('   ')
            leftrow.append(int(strings[0]))
            rightrow.append(int(strings[1]))
        return leftrow, rightrow


def distancesolver(filepath):
    leftrow, rightrow = getdatalists(filepath)
    leftrow.sort()
    rightrow.sort()
    sum = 0

    for a, b in zip(leftrow, rightrow):
        if a > b:
            sum += (a-b)
        else:
            sum += (b-a)
    return sum


def similarityscore(filepath):
    leftrow, rightrow = getdatalists(filepath)
    similaritylist = []

    for num in leftrow:
        newnum = rightrow.count(num) * num
        similaritylist.append(newnum)

    return sum(similaritylist)


print("Total distance is: " + str(distancesolver('distancevalues.txt')))
print("The similarity score is: " + str(similarityscore('distancevalues.txt')))
