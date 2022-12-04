def solution(numbers, k):
    thrower = 0
    while k > 0:
      if thrower >= len(numbers):
        thrower -= len(numbers)
      k -= 1
      thrower += 2
    return numbers[thrower - 2]