input = open("input4.txt", "r")
lines = input.readlines()

calls = str.rstrip(lines[0]).split(',')
lines = lines[2:]

boards = []
board = []

for line in lines:
    line = str.rstrip(line)
    if line == '':
        boards.append(board)
        board = []
    else:
        board.append(list(map(int, list(filter(None, line.split(' '))))))
boards.append(board)

posWins = {}

for x in range(len(boards)):
    if x not in posWins.keys():
        posWins[x] = []
    for y in range(len(boards[x])):
        posWins[x].append(boards[x][y])
        column = []
        for z in range(len(boards[x])):
            column.append(boards[x][z][y])
        posWins[x].append(column)

drawn = []
winBoard = -1
winRow = []
winNum = -1

for c in calls:
    drawn.append(int(c))
    for k in posWins.keys():
        for x in posWins[k]:
            if set(x).issubset(set(drawn)):
                winRow = x
                winBoard = k
                winNum = int(c)
                break
        if(winBoard > -1):
            break
    if(winBoard > -1):
        break

total = 0
for x in range(len(boards[winBoard])):
    for y in boards[winBoard][x]:
        if y not in drawn:
            total += y

print(total * winNum)

drawn = []
keys = list(posWins.keys())
winBoard = -1
winNum = -1

while(len(keys) > 1):
    for c in calls:
        print(len(keys))
        drawn.append((int(c)))
        for k in keys:
            win = []
            for x in posWins[k]:
                if set(x).issubset(set(drawn)):
                    keys.pop(keys.index(k))
                    if len(keys) == 0:
                        winBoard = k
                        winNum = int(c)
                    break
            if(winBoard > -1):
                break
        if(winBoard > -1):
            break

total = 0
print(boards[winBoard])
print(winNum)
for x in range(len(boards[winBoard])):
    for y in boards[winBoard][x]:
        if y not in drawn:
            total += y

print(total * winNum)
