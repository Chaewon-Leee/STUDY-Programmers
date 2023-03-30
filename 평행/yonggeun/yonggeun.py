def solution(dots):
    index_list = [0,1,2,3]
    for i in range(4):
        x1_coor, y1_coor = dots[i][0], dots[i][1]
        for j in range(4):
            x2_coor, y2_coor = dots[j][0], dots[j][1]
            try:
                slope1 = (y2_coor - y1_coor) / (x2_coor - x1_coor)
                exclude_num = [i, j]
                other_coor = [num for num in index_list if num not in  exclude_num]
                third = other_coor[0]
                fourth = other_coor[1]
                x3_coor, y3_coor = dots[third][0], dots[third][1]
                x4_coor, y4_coor = dots[fourth][0], dots[fourth][1]
                slope2 = (y4_coor - y3_coor) / (x4_coor - x3_coor)
                if slope1 == slope2:
                    return 1
            except:
                pass
    return 0


dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
print(solution(dots))