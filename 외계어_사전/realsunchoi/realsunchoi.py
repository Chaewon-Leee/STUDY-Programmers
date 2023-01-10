import itertools


def solution(spell, dic):
    per = list(map(''.join, itertools.permutations(spell)))
    i = 0
    answer = 2
    while i < len(dic):
        if dic[i] in per:
            answer = 1
            break
        else:
            i += 1
    return answer
