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

def factorization(num):
    i = 0
    result = []
    remainder = num
    prime_factor = get_prime_factor(num)
    while remainder != 1:
        if remainder%prime_factor[i]==0:
            remainder = remainder/prime_factor[i]
            result.append(prime_factor[i])
        else:
            i += 1
    return result

def solution(a, b):
    numerator = get_factor(a)
    denominator = get_factor(b)
    greatest_factor = max(list(set(numerator) & set(denominator)))
    simple_faction = b//greatest_factor
    finite_decimal = [[],[2],[5],[2,5]]
    if list(set(factorization(simple_faction))) in finite_decimal:
        return 1
    else:
        return 2