def solution(spell, dic):
    temp = []
    for word in dic:
        for char in word:
            if char in spell:
                temp.append(char)
        if set(temp) == set(spell):
            return 1
        else:
            temp = []
    return 2