import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit

answer = ""
while n != 0:
    if n % -2 != 0:
        answer += "1"
        n //= -2 + 1
    else:
        answer += "0"
        n //= -2

print(answer[::-1])

n=int(input())
res=''

if n==0:
    print(0)
    exit
while n!=0:
    if n%(-2)!=0:
        res +='1'
        n=n//(-2)+1
    else:
        res +='0'
        n=n//(-2)

print(res[::-1])