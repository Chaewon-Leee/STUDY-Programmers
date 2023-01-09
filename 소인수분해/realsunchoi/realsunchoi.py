def solution(n):
    answer = []
    for i in range(2, n+1):
        value = []
        if n % i == 0:
            for j in range(1, i):
                if i % j == 0:
                    value.append(j)
        if len(value) == 1:
            answer.append(i)
    return answer
