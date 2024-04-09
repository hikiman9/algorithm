n = int(input())

num = 1

for i in range(n, 0, -1):
    num *= i

for i in range(len(str(num))):
    if str(num)[::-1][i] != "0":
        print(i)
        break