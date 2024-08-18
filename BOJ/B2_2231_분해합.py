n = int(input())

def sepSum(num):
    sep = num
    while num > 0:
        sep += num % 10
        num //= 10
    return sep

for i in range(1, n + 1):
    if sepSum(i) == n:
        print(i)
        break
else:
    print(0)