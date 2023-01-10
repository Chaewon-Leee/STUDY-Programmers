def factorial(num):
    fac_num = 1
    if num == 0:
        return 1
    while num != 1:
        fac_num = fac_num * num
        num -= 1
    return fac_num

def solution(balls, share):
    return int(factorial(balls) / (factorial(share) * factorial(balls - share)))