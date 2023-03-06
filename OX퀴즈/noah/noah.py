def solution(quiz):
    result = []
    for i in quiz:
        a, b = i.split("=")

        if eval(a) == int(b):
            result.append("O")
        else:
            result.append("X")
    
    return result

quiz = ["3 - 4 = -3", "5 + 6 = 11"]