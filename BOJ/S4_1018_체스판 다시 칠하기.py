chess_b = [["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ]

chess_w = [["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ]

def count_fix(arr):
    
    count_w = 0
    count_b = 0

    for i in range(8):
        for j in range(8):
            if arr[i][j] != chess_b[i][j]:
                count_b += 1
            if arr[i][j] != chess_w[i][j]:
                count_w += 1
    return min(count_w, count_b)


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

answer = []

for i in range(n - 7):
    for j in range(m - 7):
        temp = []
        for k in range(8):
            temp.append(board[i + k][j:j + 8])
        answer.append(count_fix(temp))

print(min(answer))