def solution(balls, share):
    import math
    answer = math.factorial(
        balls)/(math.factorial(balls-share)*math.factorial(share))
    return answer
