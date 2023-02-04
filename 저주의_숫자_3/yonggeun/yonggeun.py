def solution(n):
    delay = 0
    num = 1
    not_curse = 0
    while not_curse != n:
        if num % 3 == 0 or '3' in str(num):
            delay += 1
        else:
            not_curse += 1
        num += 1
    return n + delay


n = 40
print(solution(n))


