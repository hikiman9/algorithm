from collections import deque

n = int(input())
waiting = list(map(int, input().split()))
waiting = deque(waiting)

new_line = []
order = 1

while waiting or new_line:
    if waiting and waiting[0] == order:
        order += 1
        waiting.popleft()
    elif new_line and new_line[-1] == order:
        order += 1
        new_line.pop()
    elif waiting and waiting[0] != order:
        new_line.append(waiting.popleft())
    else:
        break

if waiting or new_line:
    print("Sad")
else:
    print("Nice")