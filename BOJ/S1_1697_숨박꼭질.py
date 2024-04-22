n, k = map(int, input().split())

if n <= k:
    print(k - n)

answer = 0

def hands(i, j):
    if i * 2 == j or i + 1 == j or i - 1 == j:
        answer += 1
        return answer
    