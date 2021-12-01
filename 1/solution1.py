input = open("input1.txt", "r")
lines = input.readlines()

# Helper


def stripper(n):
    return int(str.rstrip(n))


lines = list(map(stripper, lines))

# Part 1
increase = 0
previous = lines[0]
for line in lines:
    num = line
    if num > previous:
        increase += 1
    previous = num

print(increase)

# Part 2
windowIncrease = 0
window1 = lines[0] + lines[1] + lines[2]
for x in range(3, len(lines)):
    window2 = window1 - lines[x-3] + lines[x]
    if window2 > window1:
        windowIncrease += 1
    window1 = window2
print(windowIncrease)
