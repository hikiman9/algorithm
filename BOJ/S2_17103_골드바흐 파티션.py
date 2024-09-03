# n = int(input())

# def soe(k):
#     primes = [True] * (k + 1)

#     primes[0] = primes[1] = False

#     i = 2
#     while i * i <= k:
#         if primes[i]:
#             for j in range(i * i, k + 1, i):
#                 primes[j] = False
#         i += 1
    
#     return [i for i in range(k + 1) if primes[i]]

# for __ in range(n):
#     answer = 0
#     num = int(input())
#     primes = soe(num)
#     print(primes)
#     i, j = 0, len(primes) - 1
#     while i <= j:
#         if primes[i] + primes[j] == num:
#             answer += 1
#             i += 1
#             j -= 1
#         if primes[i] + primes[j] > num:
#             j -= 1
#         if primes[i] + primes[j] < num:
#             i += 1
#     print(answer)

def sieve_of_eratosthenes(k):
    primes = [True] * (k + 1)
    primes[0] = primes[1] = False
    
    i = 2
    while i * i <= k:
        if primes[i]:
            for j in range(i * i, k + 1, i):
                primes[j] = False
        i += 1
    
    return [x for x in range(k + 1) if primes[x]]

# 최대 입력값에 대한 소수를 미리 구해둠
max_value = 1000000
primes = sieve_of_eratosthenes(max_value)

n = int(input())
for __ in range(n):
    num = int(input())
    answer = 0
    i, j = 0, len(primes) - 1

    # 소수 리스트 중 num 이하의 범위까지만 사용
    while i <= j and primes[j] > num:
        j -= 1

    while i <= j:
        if primes[i] + primes[j] == num:
            answer += 1
            i += 1
            j -= 1
        elif primes[i] + primes[j] > num:
            j -= 1
        else:
            i += 1

    print(answer)
