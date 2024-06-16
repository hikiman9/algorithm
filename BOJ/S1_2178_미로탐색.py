import sys
from collections import deque

n, m = map(int, input().split())
maze = []
for __ in range(n):
    maze.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x, y):
    
    qqq = deque()
    qqq.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while qqq:
        x, y = qqq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                qqq.append((nx, ny))

bfs(0, 0)

print(maze[n - 1][m - 1])