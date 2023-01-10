def is_sosu(number):
    sosu_list = []
    for i in range(1, number+1):
        if number % i == 0:
            sosu_list.append(i)
    if len(sosu_list) == 2:
        return True
    else:
        return False

def solution(n):
    answer = []
    for i in range(2,n+1):
        if n % i == 0 and is_sosu(i):
            answer.append(i)
    return answer