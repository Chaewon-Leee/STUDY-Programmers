def solution(my_string):
    number = []
    answer = 0
    my_number = '0'
    for i in my_string+'.':
        if i.isnumeric():
            my_number += i
        else:
            number.append(my_number)
            my_number = '0'
    for j in number:
        answer += int(j)
    return answer
