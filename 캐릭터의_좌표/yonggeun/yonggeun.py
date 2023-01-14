def solution(keyinput, board):
    coor_x , coor_y = 0, 0
    x_range = list(range(-int(board[0]/2), int(board[0]/2) + 1))
    y_range = list(range(-int(board[1]/2), int(board[1]/2) + 1))
    for key in keyinput:
        if key == "up":
            coor_y += 1
        elif key == "down":
            coor_y -= 1
        elif key == "right":
            coor_x += 1
        elif key == "left":
            coor_x -= 1

        if coor_x > 0 and coor_x not in x_range:
            coor_x -= 1
        elif coor_x < 0 and coor_x not in x_range:
            coor_x += 1
        elif coor_y > 0 and coor_y not in y_range:
            coor_y -= 1
        elif coor_y < 0 and coor_y not in y_range:
            coor_y += 1

    return [coor_x, coor_y]
