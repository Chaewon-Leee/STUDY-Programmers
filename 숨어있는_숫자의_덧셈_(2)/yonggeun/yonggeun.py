def solution(my_string):
    answer = 0
    my_new_string = ''
    str_num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    my_string_list = list(my_string)
    for i, my_char in enumerate(my_string_list):
        if my_char not in str_num_list:
            my_char = "+"
            my_new_string += my_char
        else:
            pass
            my_new_string += my_char
    my_num_list = my_new_string.split('+')
    for i, my_num in enumerate(my_num_list):
        if my_num != '':
            my_int_num = int(my_num)
            answer += my_int_num
        else:
            pass
    return answer