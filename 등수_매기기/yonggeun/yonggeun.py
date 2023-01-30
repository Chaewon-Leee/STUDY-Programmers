def solution(score):
    student_score_sum = []
    student_rank = []
    for student in score:
        student_sum = student[0] + student[1]
        student_score_sum.append(student_sum)
    student_reverse = sorted(student_score_sum, reverse=True)
    for i in student_score_sum:
        student_rank.append(student_reverse.index(i) + 1)
    return student_rank


score = [[80, 70], [90, 50], [40, 70], [50, 80]]
print(solution(score))
