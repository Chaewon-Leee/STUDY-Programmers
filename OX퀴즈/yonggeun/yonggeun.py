def solution(quiz):
    result = []
    for expression in quiz:
        a = expression.split('=')
        problem = a[0]
        answer = a[1]
        if eval(problem) == int(answer):
            result.append("O")
        else:
            result.append("X")
    return result

quiz = ["3 - 4 = -3", "5 + 6 = 11"]

print(solution(quiz))