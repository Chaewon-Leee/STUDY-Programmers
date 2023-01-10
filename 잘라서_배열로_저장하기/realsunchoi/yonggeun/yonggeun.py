import math
def solution(my_str, n):
    answer = []
    my_string_length = len(my_str)
    index_count = math.ceil(my_string_length / n)
    for i in range(index_count):
        sliced_str = my_str[n*i:n*(i+1)]
        answer.append(sliced_str)
    return answer