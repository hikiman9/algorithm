import sys

n = int(sys.stdin.readline())

lst = []

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if "push" in cmd:
        a, b = cmd.split()
        lst.append(int(b))
    elif cmd == "pop":
        if lst:
            a = lst.pop()
            print(a)
        else:
            print(-1)
    elif cmd == "size":
        print(len(lst))
    elif cmd == "empty":
        print(1 - int(bool(lst)))
    else:
        if lst:
            print(lst[-1])
        else:
            print(-1)