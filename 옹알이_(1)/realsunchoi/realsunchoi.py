def solution(babbling):
    count = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for can in can_speak:
            bab = bab.replace(can, ".")
        if len(bab.replace(".", "")) == 0:
            count += 1
    return count