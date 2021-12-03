input = open("input3.txt", "r")
lines = input.readlines()
binDict = {}

for line in lines:
    strippedLine = str.rstrip(line)
    for x in range(len(strippedLine)):
        if x not in binDict.keys():
            binDict[x] = [0, 0]
        if strippedLine[x] == '0':
            binDict[x][0] = binDict[x][0] + 1
        else:
            binDict[x][1] = binDict[x][1] + 1

gamma = ''
epsilon = ''

for key in binDict.keys():
    if binDict[key][0] > binDict[key][1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))
