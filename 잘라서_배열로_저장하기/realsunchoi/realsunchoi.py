import math


def solution(my_str, n):
    answer = []
    k = 0
    for i in range(math.ceil(len(my_str)/n)):
        if k+n < len(my_str):
            answer.append(my_str[k:k+n])
            k += n
        else:
            answer.append(my_str[k:])
    return answer
