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