words = input()

answer = ""

for i in words:
    if ord(i) == 32 or i.isdigit():
        answer += i
    elif i.isupper():
        if ord(i) < 78:
            answer += chr(ord(i) + 13)
        else:
            answer += chr((ord(i) + 13) % 91 + 65)
    else:
        if ord(i) < 110:
            answer += chr(ord(i) + 13)
        else:
            answer += chr((ord(i) + 13) % 123 + 97)
        
print(answer)
