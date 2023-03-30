from itertools import combinations

def solution(dots):
    gradient = []
    combination = list(combinations(dots, 2))

    for combin in combination:
      gradient.append(get_gradient(combin))

    # 기울기 중 0 제거
    gradient = [i for i in gradient if i]

    if len(gradient) == len(set(gradient)):
      return 0
    else:
      return 1

def get_gradient(dots):
  a1, b1 = dots[0]
  a2, b2 = dots[1]
  return (b2 - b1) / (a2 - a1)

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
# print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))