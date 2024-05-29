import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
field = []
for __ in range(m):
    field.append(list(sys.stdin.readline().strip()))

def ally(x, y):
    global count
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if field[y][x] == "B":
        field[y][x] = "o"
        count += 1
        ally(x, y + 1)
        ally(x + 1, y)
        ally(x, y - 1)
        ally(x - 1, y)
        return True
    return False

def enemy(x, y):
    global count
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if field[y][x] == "W":
        field[y][x] = "o"
        count += 1
        enemy(x, y + 1)
        enemy(x + 1, y)
        enemy(x, y - 1)
        enemy(x - 1, y)
        return True
    return False

allies = []
enemies = []

for i in range(n):
    for j in range(m):
        count = 0
        if field[j][i] == "B":
            ally(i, j)
            allies.append(count)
        if field[j][i] == "W":
            enemy(i, j)
            enemies.append(count)

en = sum([i ** 2 for i in enemies])
al = sum([i ** 2 for i in allies])
print(en, al)