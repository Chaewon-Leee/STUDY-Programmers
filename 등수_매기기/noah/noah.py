def solution(score):
    answer = []
    rank = []
    for i in score:
        answer.append(sum(i)/len(i))
    sort_list = (sorted(answer, reverse= True))
    # for index_i, i in enumerate(answer):
    #     for index_j, j in enumerate (sort_list):
    #         print("i: ",i,"j: ",j)
    #         if i == j:
    #             answer[index_i] = index_j + 1
    for i in answer:
        rank.append(sort_list.index(i) + 1)
    return rank



score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))

