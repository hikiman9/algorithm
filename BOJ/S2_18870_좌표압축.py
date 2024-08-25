n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

index_arr = {}
for i in range(len(arr2)):
    index_arr[arr2[i]] = i

for i in arr:
    print(index_arr[i], end=" ")