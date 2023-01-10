def solution(my_string):
    answer = 0
    ind = [0, 0]
    for i in range(len(my_string)):
        if my_string[i] == "+" and ind[0] == 0:
            answer += int(''.join(my_string[ind[1]:i]).replace(" ", ""))
            ind = [0, i+1]
        elif my_string[i] == "-" and ind[0] == 0:
            answer += int(''.join(my_string[ind[1]:i]).replace(" ", ""))
            ind = [1, i+1]
        elif my_string[i] == "+" and ind[0] == 1:
            answer -= int(''.join(my_string[ind[1]:i]).replace(" ", ""))
            ind = [0, i+1]
        elif my_string[i] == "-" and ind[0] == 1:
            answer -= int(''.join(my_string[ind[1]:i]).replace(" ", ""))
            ind = [1, i+1]

    if ind[0] == 0:
        answer += int(''.join(my_string[ind[1]:]).replace(" ", ""))
    else:
        answer -= int(''.join(my_string[ind[1]:]).replace(" ", ""))

    return answer
