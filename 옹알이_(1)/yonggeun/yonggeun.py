def solution(babbling):
    cant_speak_list = []
    count = 0
    for baby_word in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            baby_word = baby_word.replace(word, " ")
        cant_speak_list.append(baby_word)
    for word in cant_speak_list:
        if word.isspace():
            count += 1
    return count

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))