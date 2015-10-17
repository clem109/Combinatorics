__author__ = 'clementvenard'

# Please put the file input.txt in the same directory, once the program has run it will create the output in file named
# output.txt
#

f = open('output.txt', 'r+')
f.truncate()


List = open("input.txt").read().splitlines()
listLength = len(List)
listPos = 0

for i in range(listLength):
    outputLines = []
    StringUnderTest = List[listPos]
    listPos += 1
    ListUnderTest = StringUnderTest.split()
    ListUnderTest = [int(i) for i in ListUnderTest]
    x = ListUnderTest[0]
    y = ListUnderTest[1]
    n = ListUnderTest[2]
    count = 1

    if x > 20 or x == 0 or y > 20 or y == 0 or n > 100 or n < 21:
        outputLines = []
    else:
        for z in range(n):
            if (count % x == 0) & (count % y != 0):
                outputLines.append("F")
                count += 1

            elif (count % y == 0) & (count % x != 0):
                outputLines.append("B")
                count += 1

            elif (count % y == 0) & (count % x == 0):
                outputLines.append("FB")
                count += 1

            else:
                outputLines.append(count)
                count += 1

    if len(outputLines) > 0:
        outputLines = ' '.join(str(e) for e in outputLines)
        outputFile = open("output.txt", 'a')
        outputFile.write(outputLines + '\n')






