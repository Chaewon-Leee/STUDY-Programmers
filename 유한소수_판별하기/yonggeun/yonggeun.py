# 1. 기약분수로 만들기 -> 최대공약수로 나누기
# 2. 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재하면 return 1, 아니면 return 2

def find_divisor(num): # 약수 찾는 함수
    divisor = []
    i = 1
    while i <= num:
        if num % i == 0:
            divisor.append(i)
        i += 1
    return divisor

def find_greatest_common_divisor(a, b):  # 최대공약수 찾는 함수
    return [*set(find_divisor(a)) & set(find_divisor(b))][-1]

def solution(a, b):
    divided_b = b / find_greatest_common_divisor(a, b)
    while divided_b != 1:
        if divided_b % 2 == 0:
            divided_b = divided_b / 2
            continue
        elif divided_b % 5 == 0:
            divided_b = divided_b / 5
            continue
        return 2
    return 1

a, b = 12, 21
print(solution(a, b))
