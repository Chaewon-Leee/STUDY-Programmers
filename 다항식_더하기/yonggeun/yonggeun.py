def solution(polynomial):
    coefficient_sum = 0
    nums = 0
    terms = polynomial.split(" ")

    for term in terms:
        if 'x' in term:
            coefficient = term.replace("x", "")
            if coefficient == '':
                coefficient = 1
            coefficient_sum += int(coefficient)
            
        elif term == '+':
            continue
        else:
            nums += int(term)   
    xs = str(coefficient_sum) + 'x'
    str_nums = str(nums)
    if xs == '0x':
        return str_nums
    elif xs == '1x':
        xs = 'x'
    
    if str_nums == '0':
        return xs
    
    return xs + ' + ' + str_nums

polynomial = "0x + 7"
print(solution(polynomial))