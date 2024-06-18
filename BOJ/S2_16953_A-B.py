from collections import deque

a, b = map(int, input().split())

qq = deque([(a, 1)]) 
found = False

while qq:
    current, n = qq.popleft()
    
    x1 = current * 10 + 1
    x2 = current * 2
    
    if x1 == b or x2 == b:
        print(n + 1)
        found = True
        break
    
    if x1 < b:
        qq.append((x1, n + 1))
    
    if x2 < b:
        qq.append((x2, n + 1))

if not found:
    print(-1)