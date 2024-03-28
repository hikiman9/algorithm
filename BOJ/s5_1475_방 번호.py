import sys

number = sys.stdin.readline().strip()

cnt = []

for i in range(10):
    cnt.append(number.count(str(i)))

print(cnt)