def solution(quiz):
    answer = []
    result = {False:"X", True:"O"}
    for i in quiz:
        question = i.split("=")
        answer.append(result[eval(question[0]) == int(question[1])])
    return answer
        
        