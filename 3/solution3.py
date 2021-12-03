input = open("input3.txt", "r")
lines = input.readlines()
binDict = {}
lineArray = []

for line in lines:
    strippedLine = str.rstrip(line)
    lineArray.append(strippedLine)
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


def helper(lineArr, x):
    zero = 0
    one = 0
    for line in lineArr:
        if line[x] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        return 0
    elif one > zero:
        return 1
    else:
        return -1


oxArr = lineArray
co2Arr = lineArray
oxVal = ''
co2Val = ''

for x in range(len(lineArray[0])):
    if(helper(oxArr, x) == 0):
        oxArr = list(filter(lambda o: o[x] == '0', oxArr))
    else:
        oxArr = list(filter(lambda o: o[x] == '1', oxArr))
    if(helper(co2Arr, x) == 0):
        co2Arr = list(filter(lambda o: o[x] == '1', co2Arr))
    else:
        co2Arr = list(filter(lambda o: o[x] == '0', co2Arr))
    if len(oxArr) == 1:
        oxVal = oxArr[0]
    if len(co2Arr) == 1:
        co2Val = co2Arr[0]

print(int(oxVal, 2) * int(co2Val, 2))
