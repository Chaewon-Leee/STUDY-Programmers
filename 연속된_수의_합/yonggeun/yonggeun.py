def append_to_list(result, num):
    while len(result) != num:
            first_term = int(result[0] - 1)
            last_term = int(result[-1] + 1)
            result.insert(0, first_term)
            result.append(last_term)

def solution(num, total):
    result = []
    if num % 2 == 1:
        median = total / num
        result.append(int(median))
        append_to_list(result, num)
        return result
    else:
        median = total / num
        result.append(int(median - 0.5))
        result.append(int(median + 0.5))
        print(result)
        append_to_list(result, num)
        return result
    

num = 4
total = 14

print(solution(num, total))