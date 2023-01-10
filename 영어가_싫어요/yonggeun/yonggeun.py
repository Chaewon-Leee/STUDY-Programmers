def solution(numbers):
    answer = None
    temp = ''
    new_number = ''
    new_number_list = []
    numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for character in numbers:
        temp += character  # temp에 character을 한글자씩 넣으면서 numbers_list에 temp가 있는지 확인한다. 
        if temp in numbers_list:  # 만약 temp가 numbers_list 안에 있다면
            new_number_list.append(temp)  # new_number_list에 temp를 넣어준다.
            temp = ''   # temp는 초기화 시켜준다.
    for number in new_number_list:
        if number == 'zero':
            new_number += '0'
        elif number == 'one':
            new_number += '1'
        elif number == 'two':
            new_number += '2'
        elif number == 'three':
            new_number += '3'
        elif number == 'four':
            new_number += '4'
        elif number == 'five':
            new_number += '5'
        elif number == 'six':
            new_number += '6'
        elif number == 'seven':
            new_number += '7'
        elif number == 'eight':
            new_number += '8'
        elif number == 'nine':
            new_number += '9'
    answer = int(new_number)
    return answer