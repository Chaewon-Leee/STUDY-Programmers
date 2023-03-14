def solution(numer1, denom1, numer2, denom2):
    answer = []

    times_denom = denom1 * denom2

    ## 분자 구하기
    numer1 = numer1 * (times_denom / denom1)
    numer2 = numer2 * (times_denom / denom2)
    numer = numer1 + numer2

    ## 약수 구하기
    divisor_1, divisor_2 = get_divisor(numer), get_divisor(times_denom)

    ## 최대 공약수 구하기
    common_divisor = [a for a in divisor_1 if a in divisor_2]


    if not common_divisor:
      return [int(numer), times_denom]
    else:
      numer = [numer/i for i in common_divisor if numer % i == 0][-1]
      times_denom = [times_denom/i for i in common_divisor if times_denom % i == 0][-1]
      return [int(numer), int(times_denom)]

def get_divisor(num):
  divisor = []
  divisor_num = 2
  while num >= divisor_num:
    if num % divisor_num == 0: # 약수일 경우,
      divisor.append(divisor_num)
    divisor_num += 1
  return divisor

print(solution(1, 2, 3, 4))
print(solution(1, 9, 3, 6))
print(solution(9, 2, 1, 3))