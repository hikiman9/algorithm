from collections import deque

n = int(input())

arr = deque([i + 1 for i in range(n)])

status = True
while len(arr) > 1:
    if status:
        arr.popleft()
    else:
        arr.append(arr.popleft())
    status = not status

print(arr[0])