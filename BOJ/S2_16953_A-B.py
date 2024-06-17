from collections import deque

a, b = map(int, input().split())

qq = deque()
qq.append([a])

esc = False
n = 1

while qq:
    new = []
    nums = qq.popleft()
    for i in nums:
        x1 = i * 10 + 1
        x2 = i * 2
        if x1 == b or x2 == b:
            print(n + 1)
            esc = True
            break
        new.append(x1)
        new.append(x2)
    if esc:
        break
    if n > 11:
        print(-1)
        break
    qq.append(new)
    n += 1