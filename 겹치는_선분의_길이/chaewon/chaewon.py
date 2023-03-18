from itertools import combinations

def solution(lines):
  available_combination = list(combinations([0, 1, 2], 2)) # [(0, 1), (0, 2), (1, 2)]

  ## 모든 원소 뽑기
  elements = []
  for line in lines:
    elements.append([i for i in range(line[0], line[1]+1)])

  ## 겹치는 구간
  overlap_element = []
  for com in available_combination:
    overlap_element.append(get_intersection(elements[com[0]], elements[com[1]]))

  ## 선분 길이 구하기
  length = 0
  for line in overlap_element:
    if line:
      length += max(line) - min(line)

  ## 선분이 겹치는 부분
  delete_length = 0
  for com in available_combination:
    intersection_list = get_intersection(overlap_element[com[0]], overlap_element[com[1]])
    if overlap_element[com[1]] and len(intersection_list) > 2:
      overlap_element[com[1]] = list(set(overlap_element[com[1]]) - set(intersection_list))
      delete_length += max(intersection_list) - min(intersection_list)

  return length - delete_length

def get_intersection(list1, list2): # 교집합
  intersection_list = list(set(list1) & set(list2))
  return intersection_list

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))
print(solution([[0, 2], [-3, -1], [-2, 1]]))