def sugar_delivery(n):
    bag = 0
    while n >= 0:
        if n % 5 == 0: 
            bag += (n // 5)  
            return bag
        n -= 3  
        bag += 1
    return -1  

n = int(input())

print(sugar_delivery(n))

