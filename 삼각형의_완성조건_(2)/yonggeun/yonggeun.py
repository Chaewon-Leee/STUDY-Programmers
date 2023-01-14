def solution(sides):
    count = 0
    idx = 1
    while idx < 10000:
        sides.append(idx)
        sides.sort()
        if sides[2] < sides[0] + sides[1]:
            count += 1
        sides.remove(idx)
        idx += 1
    return count
