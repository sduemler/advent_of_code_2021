from typing import TYPE_CHECKING


input = open("input5.txt", "r")
inputs = input.readlines()

field = {}
lines = []

for line in inputs:
    line = str.rstrip(line).split(" -> ")
    line[0] = list(map(int, line[0].split(",")))
    line[1] = list(map(int, line[1].split(",")))
    lines.append(line)

for line in lines:
    if(line[0][0] == line[1][0]):
        xs = [line[0][1], line[1][1]]
        for y in range(min(xs), max(xs)+1):
            if (str([line[0][0], y]) not in field.keys()):
                field[str([line[0][0], y])] = 1
            else:
                field[str([line[0][0], y])] = field[str([line[0][0], y])] + 1
    elif(line[0][1] == line[1][1]):
        ys = [line[0][0], line[1][0]]
        for x in range(min(ys), max(ys)+1):
            if (str([x, line[0][1]]) not in field.keys()):
                field[str([x, line[0][1]])] = 1
            else:
                field[str([x, line[0][1]])] = field[str([x, line[0][1]])] + 1

print(len(field.values()) - list(field.values()).count(1))
