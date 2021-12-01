input = open("input1.txt", "r")
lines = input.readlines()
increase = 0
previous = int(str.rstrip(lines[0]))
lines = lines[1:]

for line in lines:
    num = int(str.rstrip(line))
    if num > previous:
        increase += 1
    previous = num

print(increase)
