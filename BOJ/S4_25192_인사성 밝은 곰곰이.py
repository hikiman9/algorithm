n = int(input())

log = {}
gom = 0

for __ in range(n):
    chat = input()
    if chat == "ENTER":
        log = {}
    elif chat not in log:
        log[chat] = 1
        gom += 1
    else:
        continue

print(gom)