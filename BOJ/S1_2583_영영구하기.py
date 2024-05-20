import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global count
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if area[x][y] == 1:
        count += 1
        area[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

n, m ,k = map(int, input().split())

area = []
for __ in range(m):
    area.append([1] * n)

for __ in range(k):
    a1, b1, a2, b2 = map(int, input().split())
    for i in range(a1, a2):
        for j in range(b1, b2):
            area[i][j] = 0

answer = []
for i in range(m):
    for j in range(n):
        count = 0
        if area[i][j] == 1:
            dfs(i, j)
            answer.append(count)

for i in sorted(answer):
    print(i, end=" ")