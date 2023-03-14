import math

def solution(num, total):
    center = total // num
    first = center - math.ceil(num / 2) + 1
    end = center + (num // 2) + 1
    return [num for num in range(first, end)]