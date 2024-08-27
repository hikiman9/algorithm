a, b = map(int, input().split())

c, d = a, b

while d > 0:
    c, d = d, c % d

print(a * b // c)