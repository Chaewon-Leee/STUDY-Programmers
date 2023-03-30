import re
def solution(babbling):
    result_list = []
    count = 0
    for i in babbling:
        temp = re.split(r'aya|ye|woo|ma',i)
        temp = ''.join(temp).split()
        result_list.append(temp)
    for i in result_list:
        if i == []:
            count += 1
    return count

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))