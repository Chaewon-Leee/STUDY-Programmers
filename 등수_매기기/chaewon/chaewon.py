def solution(score):
    ranking = score # score 크기만큼 리스트 init

    avg_score_list = sorted(score, key=lambda x: sum(x)/2, reverse=True)
    before_avg_score = 0

    for rank, avg_score in enumerate(avg_score_list):
      present_ind = score.index(avg_score) # score에서의 기존 index
      present_avg_score = sum(avg_score)/2

      if before_avg_score == present_avg_score:
        ranking[present_ind] = ranking[before_ind]

      else:
        ranking[present_ind] = rank + 1 # 등수 부여

      before_avg_score = present_avg_score
      before_ind = present_ind
    return score