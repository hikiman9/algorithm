import sys
sys.setrecursionlimit(100000)

r, c = map(int, input().split())

farm = []
for i in range(r):
    farm.append(list(sys.stdin.readline().strip()))

def dfs(x, y):
    
    global wolf
    global sheep

    if x >= r or x < 0 or y >= c or y < 0 or farm[x][y] == "#":
        return False
    if farm[x][y] == ".":
        farm[x][y] = "0"
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    elif farm[x][y] == "o":
        farm[x][y] = "0"
        sheep += 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    elif farm[x][y] == "v":
        farm[x][y] = "0"
        wolf += 1
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True

w, s = 0, 0

for i in range(r):
    for j in range(c):
        wolf = 0
        sheep = 0
        dfs(i, j)
        if sheep > wolf:
            s += sheep
        else:
            w += wolf

print(s, w)
