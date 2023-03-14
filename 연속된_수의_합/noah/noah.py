def solution(num, total):
    result = []
    result.append((total//num)-((num-1)//2))
    for i in range(num-1):
        result.append(result[-1]+1)
    return result
num = 5
total =  5
print(solution(num,total))