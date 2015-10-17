__author__ = 'clementvenard'

f = open('output.txt', 'r+')
f.truncate()
List = open("input.txt").read().splitlines()
listLength = len(List)
listPos = 0

for i in range(listLength):
    outputLines = []
    StringUnderTest = List[listPos]
    ListUnderTest = StringUnderTest.split()
    ListUnderTest = [int(i) for i in ListUnderTest]
    listPos += 1
    x = ListUnderTest[0]
    y = ListUnderTest[1]
    n = ListUnderTest[2]
    count = 1

    for z in range(n):

        if (count % x == 0) & (count % y != 0):
            outputLines.append("F")
            count += 1

        elif (count % y == 0) & (count % x != 0):
            outputLines.append("B")
            count += 1

        elif (count % x == 0) & (count % y == 0):
            outputLines.append("FB")
            count += 1
        else:
            outputLines.append(count)
            count += 1

    outputLines = ' '.join(str(e) for e in outputLines)
    outputFile = open("output.txt", 'a')
    outputFile.write(outputLines + '\n')
    z = 0

    open("output.txt")



