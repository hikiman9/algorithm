n = int(input())

i = 1
while i * i < n:
    i += 1

if n == 1:
    print(1)
else:
    print(i - 1)