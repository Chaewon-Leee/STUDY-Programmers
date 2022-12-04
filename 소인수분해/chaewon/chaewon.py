def solution(n):
    answer = []
    for num in range(2, n+1):
      while n%num == 0:
        n = n/num
        answer.append(num)
      if n == 1:
        break
    deduplication_list = list(set(answer))
    return sorted(deduplication_list)