#  Author: Silas Lenz

board = []
for i in range(4):
    board.append([int(x) for x in input().split()])
direction = int(input())
# print(board)

# print("Direction:", direction)
if direction == 0:
    # left
    board = [[x for x in y if x != 0] for y in board]
    previous = 0
    for rowid in range(4):
        previous = 0
        for i, item in enumerate(board[rowid]):
            if (previous == item):
                board[rowid][i - 1] = item * 2
                board[rowid][i] = 0
                previous = 0
            else:
                previous = item
    board = [[x for x in y if x != 0] for y in board]
    for x in range(4):
        for y in range(4):
            try:
                print(board[x][y], end=" ")
            except:
                print("0", end=" ")
        print()
elif direction == 1:
    # up
    board = [*zip(*board)]
    # print(board)
    board = [[x for x in y if x != 0] for y in board]
    previous = 0
    for rowid in range(4):
        previous = 0
        for i, item in enumerate(board[rowid]):
            if (previous == item):
                board[rowid][i - 1] = item * 2
                board[rowid][i] = 0
                previous = 0
            else:
                previous = item
    board = [[x for x in y if x != 0] for y in board]
    for row in range(4):
        board[row] = board[row] + [0] * (4 - len(board[row]))
    # print("after padding", board)
    board = [*zip(*board)]
    # print(board)
    for x in range(4):
        for y in range(4):
            try:
                print(board[x][y], end=" ")
            except:
                print("0", end=" ")
        print()
elif direction == 2:
    # right
    board = [[x for x in y if x != 0] for y in board]
    previous = 0
    for rowid in range(4):
        previous = 0
        reversed_row = list(reversed(board[rowid]))
        for i, item in enumerate(reversed(board[rowid])):
            if (previous == item):
                reversed_row[(i - 1)] = item * 2
                reversed_row[i] = 0
                previous = 0
            else:
                previous = item
        board[rowid] = reversed(reversed_row)
    board = [[x for x in y if x != 0] for y in board]
    for row in range(4):
        board[row] = [0] * (4 - len(board[row])) + board[row]
    for x in range(4):
        for y in range(4):
            try:
                print(board[x][y], end=" ")
            except:
                print("0", end=" ")
        print()
elif direction == 3:
    # down
    board = [*zip(*board)]
    # print(board)
    board = [[x for x in y if x != 0] for y in board]
    previous = 0
    for rowid in range(4):
        previous = 0
        for i, item in enumerate(board[rowid]):
            if (previous == item):
                board[rowid][i - 1] = item * 2
                board[rowid][i] = 0
                previous = 0
            else:
                previous = item
    board = [[x for x in y if x != 0] for y in board]
    for row in range(4):
        board[row] =  [0] * (4 - len(board[row])) +  board[row]
    # print("after padding", board)
    board = [*zip(*board)]
    # print(board)
    for x in range(4):
        for y in range(4):
            try:
                print(board[x][y], end=" ")
            except:
                print("0", end=" ")
        print()
