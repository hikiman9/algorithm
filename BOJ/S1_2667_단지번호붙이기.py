import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if area[x][y] == 1:
        
        count += 1
        area[x][y] = 0

        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)

        return True
    
    return False


n = int(input())

area = []
for i in range(n):
    line = list(input())
    area.append(list(map(int, line)))

answer = []

for i in range(n):
    for j in range(n):
        count = 0
        if area[i][j] == 1:
            dfs(i, j)
            answer.append(count)


print(len(answer))
for i in sorted(answer):
    print(i)