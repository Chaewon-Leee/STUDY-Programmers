def solution(keyinput, board):
    keyinput_num = []
    for i in keyinput:
        if i == "left":
            keyinput_num.append([-1,0])
        elif i == "right":
            keyinput_num.append([1,0])
        elif i == "up":
            keyinput_num.append([0,1])
        elif i == "down":
            keyinput_num.append([0,-1])
    board_X, board_Y = board
    X, Y = [0,0]
    for i in keyinput_num:
        keyinput_X, keyinput_Y = i
        if abs(X+keyinput_X)  <= (board_X-1)//2 and abs(Y+keyinput_Y) <= (board_Y-1)//2 :
            X += keyinput_X
            Y += keyinput_Y
        print(X,Y)
    return [X,Y]

keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]
print(solution(keyinput,board))
