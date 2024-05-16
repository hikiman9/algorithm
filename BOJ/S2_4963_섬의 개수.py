import sys
sys.setrecursionlimit(10000)

def dfs(a, b):
    if a < 0 or a >= x or b < 0 or b >= y:
        return False
    
    if land[a][b] == 1:

        land[a][b] = 0
        
        dfs(a, b + 1)
        dfs(a + 1, b)
        dfs(a, b - 1)
        dfs(a - 1, b)
        dfs(a + 1, b + 1)
        dfs(a + 1, b - 1)
        dfs(a - 1, b + 1)
        dfs(a - 1, b - 1)
        
        return True
    
    return False

while True:
    y, x = map(int, input().split())
    if x + y == 0:
        break
    
    count = 0
    land = []
    for i in range(x):
        land.append(list(map(int, input().split())))

    for i in range(x):
        for j in range(y):
            if dfs(i, j):
                count += 1
    
    print(count)