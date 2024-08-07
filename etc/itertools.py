import itertools

arr = [1, 2, 3, 4]

a = itertools.combinations(arr, 2) # 조합
b = itertools.permutations(arr, 2) # 순열

print(a) # <itertools.combinations object at 0x000001D2ACF33A10>
print(b) # <itertools.permutations object at 0x000001D2ACF33BA0>

a = list(itertools.combinations(arr, 2))
b = list(itertools.permutations(arr, 2))

print(a) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(b) # [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

print(type(a[0])) # <class 'tuple'>

a = itertools.combinations(arr, 2)
for i in a:
    print(sum(i), end=" ") # 3 4 5 5 6 7
    # 순열, 조합 객체를 꼭 배열로 변환하지 않아도 사용 가능하다

# 요소가 2개인 중복 순열
a = list(itertools.product(arr, repeat=2))
# a = list(itertools.product(arr, arr)) 와 같다
print(a) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# product는 데카르트 곱이라고도 하는 cartesian product를 표현할 때 사용하는 메소드
a = list(itertools.product(arr, "ab", "#$"))
print(a) # [(1, 'a', '#'), (1, 'a', '$'), (1, 'b', '#'), (1, 'b', '$'), (2, 'a', '#'), (2, 'a', '$'), (2, 'b', '#'), (2, 'b', '$'), (3, 'a', '#'), (3, 'a', '$'), (3, 'b', '#'), (3, 'b', '$'), (4, 'a', '#'), (4, 'a', '$'), (4, 'b', '#'), (4, 'b', '$')]

# 요소가 2개인 중복 조합
a = list(itertools.combinations_with_replacement(arr, 2))
print(a) 