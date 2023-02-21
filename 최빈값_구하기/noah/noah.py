
def solution(array):
    sorted_number_listr = sorted(list(set(array)))
    number_dict = {}
    for i in sorted_number_listr:
        number_dict[i] = array.count(i)
    max_number = max(number_dict.values())
    result_list = []
    for value, count in number_dict.items():
        if count == max_number:
            result_list.append(value)
    if len(result_list) ==1:
        return result_list[0]
    else:
        return -1
array = [1, 2, 3, 3, 3, 4]
print(solution(array))