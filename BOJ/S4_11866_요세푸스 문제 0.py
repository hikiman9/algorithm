n, k = map(int, input().split())

arr = [i for i in range(n + 1)]

i = 0
total_count = 0
yosep = []

while total_count < n:
    i_count = 0
    while i_count < k:
        if i == n:
            i = 0
        if arr[i + 1] == 0:
            i += 1
        else:
            i += 1
            i_count += 1
    yosep.append(arr[i])
    arr[i] = 0
    total_count += 1

yosep = ", ".join(list(map(str, yosep)))

print("<" + yosep + ">")