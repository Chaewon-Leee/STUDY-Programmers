def solution(dots):
  answer = 0
  xs = []
  ys = []
  for x, y in dots:
    xs.append(x)
    ys.append(y)
  width = max(xs) - min(xs)
  length = max(ys) - min(ys)
  return width * length