def merge_sort(arr, tmp, left, right, k):
    global count, result
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, tmp, left, mid, k)      # 왼쪽 부분 정렬
        merge_sort(arr, tmp, mid + 1, right, k) # 오른쪽 부분 정렬
        merge(arr, tmp, left, mid, right, k)    # 병합 과정

def merge(arr, tmp, left, mid, right, k):
    global count, result
    i, j, t = left, mid + 1, left

    # 두 부분 배열을 병합하는 과정
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
        count += 1
        if count == k:
            result = tmp[t-1]

    # 왼쪽 배열의 나머지 처리
    while i <= mid:
        tmp[t] = arr[i]
        i += 1
        t += 1
        count += 1
        if count == k:
            result = tmp[t-1]

    # 오른쪽 배열의 나머지 처리
    while j <= right:
        tmp[t] = arr[j]
        j += 1
        t += 1
        count += 1
        if count == k:
            result = tmp[t-1]

    # 병합된 배열을 원래 배열에 복사
    for i in range(left, right + 1):
        arr[i] = tmp[i]

n, k = map(int, input().split()) # 배열 크기 n과 K번째 저장된 수 k 입력
arr = list(map(int, input().split())) # 배열 입력
tmp = [0] * n
count = 0
result = -1

merge_sort(arr, tmp, 0, n - 1, k)

print(result)
