def solution(a, b):
    
    answer = []
    small = min(a, b)
    big = max(a, b)

    #최대공약수 구하기
    for i in range(small, 0, -1):
        if a % i == 0 and b % i == 0:
            answer.append(i)
            break
    
    #최소공배수 구하기
    for i in range(big, a * b + 1):
        if i % a == 0 and i % b == 0:
            answer.append(i)
            break
    
    return answer