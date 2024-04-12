from collections import deque
import sys

n = int(sys.stdin.readline())

answer = deque([])

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if "push" in cmd:
        a, b = cmd.split()
        answer.append(b)
    elif cmd == "pop":
        if answer:
            a = answer.popleft()
            print(a)
        else:
            print(-1)
    elif cmd == "size":
        print(len(answer))
    elif cmd == "empty":
        print(1 - int(bool(answer)))
    elif cmd == "front":
        if answer:
            print(answer[0])
        else:
            print(-1)
    else:
        if answer:
            print(answer[-1])
        else:
            print(-1)
            