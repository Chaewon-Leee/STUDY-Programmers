def solution(numbers, k):
    answer = 1
    for i in range(k-1):
        if answer > (len(numbers) - 2):
            answer -= len(numbers) - 2
        else:
            answer += 2
    return answer
