def solution(spell, dic):
    answer = 2
    for ind, value in enumerate(dic):
        if len(value) == len(spell):
            new_value = value
            for spelling in spell:
                new_value = new_value.replace(spelling, ' ', 1)
            dic[ind] = new_value

    check_list = [n for n in dic if not n.isspace()]  # 공백 제거

    if len(check_list) != len(dic):
        answer = 1

    return answer
