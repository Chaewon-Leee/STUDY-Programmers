def solution(array):
  mode = {}
  for integer in list(set(array)):
    mode[integer] = 0

  for integer in array:
    mode[integer] = mode[integer] + 1

  answer = [ ]
  for idx in mode.keys():
    if mode[idx] == max(mode.values()):
      answer.append(idx)

  return -1 if len(answer) > 1 else answer[0]