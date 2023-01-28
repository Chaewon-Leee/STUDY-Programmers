def solution(score):
    ranking = score # score 크기만큼 리스트 init

    avg_score_list = sorted(score, key=lambda x: sum(x)/2, reverse=True)

    before_avg_score = 0
    for rank, avg_score in enumerate(avg_score_list):
      rank_index = score.index(avg_score)
      present_avg_score = sum(avg_score)/2

      if before_avg_score == present_avg_score:
        ranking[rank_index] = ranking[rank_index-1]
      else:
        ranking[rank_index] = rank+1

      before_avg_score = present_avg_score
    return score


print(solution([[80, 70], [70, 80], [70, 80], [90, 100], [100, 90], [100, 100], [10, 30]]))