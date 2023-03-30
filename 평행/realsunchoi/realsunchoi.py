from itertools import combinations

def solution(dots):
    selected_dots = list(combinations(dots, 2))
    slope_list = []
    answer = 0

    for dot in selected_dots:
        line_1 = list(dot)
        line_2 = [x for x in dots if x not in dot]

        first_slope = - (line_1[1][1]-line_1[0][1]) / (line_1[1][0]-line_1[0][0])
        second_slope = - (line_2[1][1]-line_2[0][1]) / (line_2[1][0]-line_2[0][0])

        if first_slope == second_slope:
            answer = 1
            break
        else:
            continue

    return answer