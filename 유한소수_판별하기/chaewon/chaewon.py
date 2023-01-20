def solution(a, b):
    answer = 1

    a_divisor = get_divisor(a)
    b_divisor = get_divisor(b)

    for a_div in a_divisor:
      if a_div in b_divisor:
        b /= a_div
        b_divisor.remove(a_div)

    for i in b_divisor:
      if i == 2 or i == 5:
        pass
      else:
        answer = 2

    return answer

def get_divisor(num):
  divisor = []
  divisor_num = 2
  while num >= divisor_num:
    if num % divisor_num == 0: # 약수일 경우,
      num /= divisor_num
      divisor.append(divisor_num)
    else:
      divisor_num += 1
  return divisor

print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
