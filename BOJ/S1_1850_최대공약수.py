i, j = map(int, input().split())

def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print("1" * gdc(i, j))