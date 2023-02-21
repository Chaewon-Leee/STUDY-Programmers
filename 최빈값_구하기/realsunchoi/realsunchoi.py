def solution(array):
    unique_array = list(set(array))
    count_num = [array.count(num) for num in unique_array]
    count_mode = max(count_num)
    
    if count_num.count(count_mode) != 1:
        return -1
    else:
        return unique_array[count_num.index(count_mode)]