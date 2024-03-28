def solution(n):
    
    numbers = []
    while n > 2:
        numbers.append(n % 3)
        n //= 3
    numbers.append(n)
    
    return int("".join(list(map(str, numbers))), 3)
