import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
stack = []

output = []

for i in range(1, N + 1):
    command = data[i]
    
    if command[0] == '1':
        _, X = command.split()
        stack.append(int(X))
    
    elif command == '2':
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)
    
    elif command == '3':
        output.append(len(stack))
    
    elif command == '4':
        if stack:
            output.append(0)
        else:
            output.append(1)
    
    elif command == '5':
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)

sys.stdout.write('\n'.join(map(str, output)) + '\n')
