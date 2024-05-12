n = int(input())

d = [1] * (n + 1)

for i in range(1, n + 1):
    if i % 2 == 1:
        d[i] = (d[i - 1] * 2) - 1
    else:   
        d[i] = (d[i - 1] * 2) + 1

print(d[n] % 10007) 