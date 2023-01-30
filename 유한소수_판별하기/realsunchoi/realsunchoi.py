def get_factor(num):
    factor = [i for i in range(1,num+1) if num%i == 0]
    return factor

def get_prime_factor(num):
    prime_num = []
    for factor in get_factor(num):
        factor_list = get_factor(factor)
        if factor_list == [1,factor]:
            prime_num.append(factor)
    return prime_num

def solution(a, b):
    numerator = get_factor(a)
    denominator = get_factor(b)
    greatest_factor = max(list(set(numerator) & set(denominator)))
    simple_faction = b//greatest_factor
    finite_decimal = [[],[2],[5],[2,5]]
    if list(set(get_prime_factor(simple_faction))) in finite_decimal:
        return 1
    else:
        return 2