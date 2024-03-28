def solution(people, limit):
    
    people.sort()
    
    start = 0
    end = len(people) - 1

    answer = 0

    while start <= end:
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            answer += 1
            end -= 1
    
    return answer

solution([70, 80, 50, 50], 100)