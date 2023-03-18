def prime_factor(n):
    answer = []
    num = 2
    while n != 1:
        if n%num == 0:
            answer.append(num)
            n = n//num
            num = 2
        else :
            num = num + 1
    return sorted(answer) # 교집합 제거 x

def solution(numer1, denom1, numer2, denom2):
    result_denom = denom1 * denom2
    result_numer = numer1 * denom2 + numer2 * denom1
    denom_factor = prime_factor(result_denom)
    numer_factor = prime_factor(result_numer)

    common_factor = 1
    for i in numer_factor:
        if i in denom_factor:
            denom_factor.remove(i)
            common_factor = common_factor * i

    return [result_numer // common_factor, result_denom// common_factor]

numer1, denom1,	numer2,	denom2 = 1,	4, 3, 4
print(solution(numer1, denom1, numer2, denom2))