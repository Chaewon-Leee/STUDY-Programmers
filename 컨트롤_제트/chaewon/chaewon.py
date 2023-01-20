def solution(s):
  answer = 0
  numbers = s.split(" ")
  for ind in range(len(numbers)):
    num = numbers[ind]
    if num == "Z":
      answer -= int(numbers[ind-1])
    else:
      answer += int(num)
  return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))