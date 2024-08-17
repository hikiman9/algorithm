n = int(input())

sixs = []

for i in range(666, 6660000):
    if "666" in str(i):
        sixs.append(i)

print(sixs[n - 1])

# n = int(input())

# count = 0
# num = 666

# while True:
#     if "666" in str(num):
#         count += 1
#     if count == n:
#         print(num)
#         break
#     num += 1