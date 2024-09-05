from collections import deque

n = int(input())
qors = list(map(int, input().split()))
b = list(map(int, input().split()))
b = [deque([i]) for i in b]
m = int(input())
c = deque(map(int, input().split()))

