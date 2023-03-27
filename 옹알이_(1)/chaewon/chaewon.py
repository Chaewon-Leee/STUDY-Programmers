from itertools import permutations

def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    all_of_words = []

    ## 모든 조합 구하기
    for i in range(1, len(can_speak) +1): # 1~len길이까지
      all_of_words += [''.join(i) for i in list(permutations(can_speak, i))]

    for i in babbling:
      if i in all_of_words:
        answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
