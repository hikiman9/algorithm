# def fac(a):
#     num = 1
#     for i in range(a, 0, -1):
#         num *= i
#     return num

# n, k = map(int, input().split())

# target = fac(n) / (fac(k) * fac(n - k))
# for i in range(len(str(target))):
#     if str(target)[::-1][i] != "0":
#         print(i)
#         break
