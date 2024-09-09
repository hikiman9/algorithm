def pibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return pibonacci(n - 1) + pibonacci(n - 2)

print(pibonacci(int(input())))