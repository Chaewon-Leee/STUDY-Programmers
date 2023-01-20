def solution(s):
    answer = s.replace(" ", "+")
    answer_list = s.split(" ")
    for i in range(answer_list.count("Z")):
        index = answer_list.index("Z")
        answer_list[index] = "."
        before_num = "-" + answer_list[index-1]
        answer = answer.replace("+Z", before_num, 1)
    return eval(answer)