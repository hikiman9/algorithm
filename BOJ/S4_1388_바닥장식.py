n, m = map(int, input().split())

def dfs1(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == "-":
        floor[x][y] = "o"
        dfs1(x, y + 1)
        return True
    return False

def dfs2(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if floor[x][y] == "|":
        floor[x][y] = "o"
        dfs2(x + 1, y)
        return True
    return False

floor = []
for __ in range(n):
    floor.append(list(input()))

answer = 0
for i in range(n):
    for j in range(m):
        if floor[i][j] == "-":
            dfs1(i, j)
            answer += 1
        elif floor[i][j] == "|":
            dfs2(i, j)
            answer += 1
        else:
            continue
        print(i, j)
        print(answer)

print(answer)