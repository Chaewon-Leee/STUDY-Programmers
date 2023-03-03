from collections import Counter
def solution(array):
    if len(array) == 1:
        return array[0]

    number_counter = Counter(array).most_common()

    if len(number_counter) == 1:
        return number_counter[0][0]

    if number_counter[0][1] == number_counter[1][1]:
        return -1
    else:
        return number_counter[0][0]

array = [1, 1, 1, 1, 2, 2, 2, 2]
print(solution(array))





