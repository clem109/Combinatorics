__author__ = 'clementvenard'

count = 1

text_file = open("input.txt", "r")
lines = text_file.read().split(' ')
# converting lines into int values
lines = [int(i) for i in lines]
text_file.close()

x = lines[0]
y = lines[1]
n = lines[2]

outputLines = []

for i in range(n):

    if (count % x == 0) & (count % y != 0):
        outputLines.append("Fizz")
        count += 1

    elif (count % y == 0) & (count % x != 0):
        outputLines.append("Buzz")
        count += 1

    elif (count % x == 0) & (count % y == 0):
        outputLines.append("Fizz Buzz")
        count += 1
    else:
        outputLines.append(count)
        count += 1

outputLines = ' '.join(str(e) for e in outputLines)
outputFile = open("output.txt", 'a')
outputFile.write(outputLines)
