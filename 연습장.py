import sys

board = []
for _ in range(100):
    temp = [0] * 100
    board.append(temp)

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y+ 10):
            board[i][j] = 1

cnt = 0

for i in board:
    cnt += i.count(1)

print(cnt)