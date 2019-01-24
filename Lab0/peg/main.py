#  Author: Silas Lenz

board = []

for y in range(7):
    row = input()
    board.append([])
    for x in range(7):
        board[y].append(row[x])

# print(board)
possible = 0
for x in range(7):
    for y in range(7):
        if board[x][y] == 'o':
            try:
                if x>=2 and board[x - 1][y] == "o" and board[x - 2][y] == ".":
                    possible += 1
            except:
                pass
            try:
                if x<=4 and board[x + 1][y] == "o" and board[x + 2][y] == ".":
                    possible += 1
            except:
                pass
            try:
                if y>=2 and board[x][y - 1] == "o" and board[x][y - 2] == ".":
                    possible += 1
            except:
                pass
            try:
                if y<=5 and board[x][y + 1] == "o" and board[x][y + 2] == ".":
                    possible += 1
            except:
                pass
print(possible)
