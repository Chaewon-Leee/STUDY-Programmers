def inclination(list1, list2):
    x1, y1 = list1
    x2, y2 = list2
    return (x2 - x1)/(y2 - y1) 


def solution(dots):
    a, b, c, d = dots
    if inclination(a,b) == inclination(c, d) or\
        inclination(a,c) == inclination(b, d) or \
        inclination(a,d) == inclination(b, c):
        return 1
    else:
        return 0

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))