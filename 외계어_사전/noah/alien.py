def solution(spell, dic):
    count = 0
    result = 0
    for i in dic:
        for spelling in spell:
            if spelling in i:
                count += 1
            if count == len(spell):
                result += 1
        count = 0
    if result == 0:
        return 2
    else:
        return 1
        
dic = ["def", "dww", "dzx", "loveaw"]
spell = ["z", "d", "x"]
print(solution(spell,dic))