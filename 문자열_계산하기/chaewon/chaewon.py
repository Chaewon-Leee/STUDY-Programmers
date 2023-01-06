def solution(my_string):
    string = my_string.split(' ')
    answer = int(string[0])
    for ind in range(len(string)):
        if ind % 2 != 0:  # 연산자인 경우
            num = int(string[ind+1])
            symbol = string[ind]
            if symbol == '+':
                answer += num
            elif symbol == '-':
                answer -= num
    return answer
