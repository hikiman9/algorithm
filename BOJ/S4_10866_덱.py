from collections import deque
import sys

n = int(sys.stdin.readline())

que = deque([])

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if "push_front" in cmd:
        a, b = cmd.split()
        que.appendleft(int(b))
    elif "push_back" in cmd:
        a, b = cmd.split()
        que.append(int(b))
    elif cmd == "pop_front":
        if que:
            a = que.popleft()
            print(a)
        else:
            print(-1)
    elif cmd == "pop_back":
        if que:
            a = que.pop()
            print(a)
        else:
            print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(1 - int(bool(que)))
    elif cmd == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)