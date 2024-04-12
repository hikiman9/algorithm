n = int(input())

for _ in range(n):
    stack = []
    conc = input()

    for i in conc:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(1)
                break
    if stack:
        print("NO")
    else:
        print("YES")