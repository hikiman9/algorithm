from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 0))

answer = []

while q:

    crt, n = q.popleft()
    x1 = crt - 1
    x2 = crt + 1
    x3 = crt * 2

    if x1 == b or x2 == b or x3 == b:
        for i in [x1, x2, x3]:
            if i == b:
                answer.append(n + 1)
            else:
                q.append((i, n + 1))
    else:
        for i in [x1, x2, x3]:
            q.append((i, n + 1))
    if len(set(answer)) > 1:
        break
print(answer[0])
print(answer.count(min(answer)))