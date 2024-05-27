import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if paper[x][y] == 1:
        paper[x][y] = 0
        count += 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False

paints = []

for i in range(n):
    for j in range(m):
        count = 0
        dfs(i, j)
        if count != 0:
            paints.append(count)

if len(paints) == 0:
    print(0)
    print(0)
else:
    print(len(paints))
    print(max(paints))