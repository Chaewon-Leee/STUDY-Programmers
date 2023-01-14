def solution(dots):
    x = []
    y = []
    for point in dots:
        x.append(point[0])
        y.append(point[1])
    set_x = list(set(x))
    set_y = list(set(y))
    return abs(set_x[0] - set_x[1]) * abs(set_y[0] - set_y[1])
