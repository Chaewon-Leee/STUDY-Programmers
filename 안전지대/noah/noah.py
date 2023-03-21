import copy
def solution(board):
    # 리스트에서 1값을 찾는다
    # for문 dictionary로 바꾸기 
    board_dict = {}
    for inx, val in enumerate(board):
        board_dict[inx] = val
    result_dict = copy.deepcopy(board_dict)
    for key, value in board_dict.items():
        for i_idx, i in enumerate(value):
            if i == 1:
                try:
                    result_dict[key][i_idx-1] = 2
                except:
                    pass
                try:
                    result_dict[key][i_idx+1] = 2
                except:
                    pass
                try:
                    result_dict[key-1][i_idx-1] = 2
                except:
                    pass
                try:
                    result_dict[key-1][i_idx] = 2
                except:
                    pass
                try:
                    result_dict[key-1][i_idx+1] = 2
                except:
                    pass
                try:
                    result_dict[key+1][i_idx-1] = 2
                except:
                    pass
                try:
                    result_dict[key+1][i_idx] = 2
                except:
                    pass
                try:
                    result_dict[key+1][i_idx+1] = 2
                except:
                    pass
    num = 0
    for key, value in result_dict.items():
        for i_idx, i in enumerate(value):
            if i == 0:
                num += 1
    print(result_dict)
    return num

board = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))