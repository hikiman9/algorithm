def two(n):
    val = 0
    if n < 2:
        return 0
    while n > 1:
        val += n // 2
        n //= 2
    return val

def five(n):
    val = 0
    if n < 5:
        return 0
    while n > 1:
        val += n // 5
        n //= 5
    return val

n, k = map(int, input().split())

cnt_2 = two(n) - two(n - k) - two(k)
cnt_5 = five(n) - five(n - k) - five(k)

print(min(cnt_2, cnt_5))