import sys
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())
floor = [[0] * m for __ in range(n)]
for __ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    floor[a - 1][b - 1] = 1

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == 1:
        count += 1
        floor[x][y] = 0
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False

answer = []
for i in range(n):
    for j in range(m):
        if floor[i][j] == 1:
            count = 0
            dfs(i, j)
            answer.append(count)

print(max(answer))