def solution(sides):
    available_sides = []

    ## 가장 긴 변이 sides 안에 있는 경우,
    long_side = max(sides)
    another_side = min(sides)
    for last_side in range(long_side+1):
      if another_side + last_side > long_side:
        # print(last_side)
        available_sides.append(last_side)

    ## 가장 긴 변이 나머지 한 변인 경우,
    long_side = max(sides)
    another_side = min(sides)
    last_side = max(sides) +1
    while another_side + long_side > last_side:
      # print(last_side)
      last_side += 1
      available_sides.append(last_side)

    return len(available_sides)

print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))