input = open("input2.txt", "r")
lines = input.readlines()
directions = []
x = 0
y = 0


def formatter(n):
    line = str.rstrip(n)
    dir = line.split(" ")
    dir[1] = int(dir[1])
    directions.append(dir)


output = list(map(formatter, lines))

for i in range(len(directions)):
    dir = directions[i][0]
    dist = directions[i][1]
    if dir == 'forward':
        x += dist
    elif dir == 'down':
        y += dist
    elif dir == 'up':
        y -= dist

print(x * y)

x = 0
y = 0
aim = 0

for i in range(len(directions)):
    dir = directions[i][0]
    dist = directions[i][1]
    if dir == 'forward':
        x += dist
        y += (dist * aim)
    elif dir == 'down':
        aim += dist
    elif dir == 'up':
        aim -= dist

print(x * y)
