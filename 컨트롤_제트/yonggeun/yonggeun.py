def solution(s):
    index_list = []
    index = 1
    count = 0
    for i in s.split(" "):
        index_list.append(index)
        if i == "Z":
            i =  -int(s.split(" ")[index - 2])
        count += int(i)
        index += 1
    return count

s = "10 20 30 Z 40"
print(solution(s))