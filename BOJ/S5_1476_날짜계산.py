a, b, c = map(int, input().split())


n = 0
while True:
    if ((n * 15 + a) - b) % 28 == 0 and ((n * 15 + a) - c) % 19 == 0:
        print(n * 15 + a)
        break
    n += 1
