def solution(num, total):
    answer = 0
    if num % 2 == 0: ## 짝수일 경우
      sum_num = total/(num/2)
      mid_num_1 = sum_num//2
      start_num = int(mid_num_1 - (num//2 -1))
      end_num = int(mid_num_1 + (num//2 +1))
      answer = [i for i in range(start_num, end_num)]
    else: ## 홀수일 경우
      mid_num = total/num
      start_num = int(mid_num-(num//2))
      end_num = int(mid_num+(num//2)) + 1
      answer = [i for i in range(start_num, end_num)]
    return answer

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))