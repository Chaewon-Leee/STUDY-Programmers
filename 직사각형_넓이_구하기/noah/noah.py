def solution(dots):
    a,b,c,d = sorted(dots)
    return abs(a[1] - b[1]) * abs(a[0]-c[0])

dots = [[1, 1], [2, 1], [2, 2], [1, 2]]
solution(dots)


