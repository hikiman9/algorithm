n = int(input())
arr = sorted(list(map(int, input().split())))

if n % 2 == 1:
    print(arr[n // 2] ** 2)
else:
    print(arr[0] * arr[-1])