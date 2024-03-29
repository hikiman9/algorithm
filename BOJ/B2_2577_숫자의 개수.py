import sys

a = 1
for _ in range(3):
    a *= int(sys.stdin.readline())

for i in range(10):
    print(str(a).count(str(i)))
