def solution(score):
    ranking = score # score 크기만큼 리스트 init

    avg_score_list = sorted(score, key=lambda x: sum(x)/2, reverse=True)
    print(avg_score_list)
    before_avg_score = 0

    for rank, avg_score in enumerate(avg_score_list):
      rank_index = score.index(avg_score)
      # bf_rank_index = rank_index
      present_avg_score = sum(avg_score)/2
      print(rank_index)

      if before_avg_score == present_avg_score:
        ranking[rank_index] = ranking[rank_index-1]
        print(f'ranking : {ranking[rank_index-1]}')

      else:
        ranking[rank_index] = rank+1
        print(f'rank : {rank}')

      before_avg_score = present_avg_score
    return score

def solution_no(score):
    answer = []
    rank = []
    for i in score:
        answer.append(sum(i)/len(i))
    sort_list = (sorted(answer, reverse= True))

    for i in answer:
        rank.append(sort_list.index(i) + 1)
    return rank

# [6, 4, 4, 6, 2, 2, 1]
ans = [[80, 70], [70, 90], [90, 70], [70, 80], [90, 100], [100, 90], [100, 100]]
print(solution(ans))
# print(solution_no(ans))
# for i in range(len(ans)):
#   if solution_yong(ans) == solution(ans):
#   print(solution_yong(ans) == solution(ans))


# print(solution([[80, 70], [70, 80], [70, 80], [90, 100], [100, 90], [100, 100], [10, 30]]))