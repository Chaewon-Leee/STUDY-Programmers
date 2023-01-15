def solution(keyinput, board):
    moving = {"up":[0,1], "down":[0,-1], "left":[-1,0], "right":[1,0]}
    answer = [0,0]
    for key in keyinput:
        if abs(answer[0]+moving[key][0]) > ((board[0]-1)/2) or abs(answer[1]+moving[key][1]) > ((board[1]-1)/2):
            continue
        else:
            answer[0] += moving[key][0]
            answer[1] += moving[key][1]
    return answer