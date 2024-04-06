import sys

while True:
    temp = [0, 0, 0, 0]
    try:
        sent = input()
        for i in sent:
            if i.islower():
                temp[0] += 1
            elif i.isupper():
                temp[1] += 1
            elif i.isdigit():
                temp[2] += 1
            else:
                temp[3] += 1
        print(temp[0], temp[1], temp[2], temp[3])
    except:
        break