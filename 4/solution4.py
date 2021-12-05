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
        board.append(list(filter(None, line.split(' '))))
