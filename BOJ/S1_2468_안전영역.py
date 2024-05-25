import sys
import copy
sys.setrecursionlimit(10000)

def dfs(x, y, limit):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] > limit:
        
        graph[x][y] = limit - 1

        dfs(x, y + 1, limit)
        dfs(x, y - 1, limit)
        dfs(x + 1, y, limit)
        dfs(x - 1, y, limit)

        return True
    
    return False


n = int(input())

area = []
for _ in range(n):
    area.append(list(map(int, sys.stdin.readline().split())))


count = []
for i in range(1, 101):
    graph = copy.deepcopy(area)
    safe = 0
    for j in range(n):
        for k in range(n):
            if dfs(j, k, i):
                safe += 1
    count.append(safe)
 
answer = max(1, max(count))

print(answer)