import math

def lcm(a,b):  # 최소공배수
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    lcm_of_denoms = lcm(denom1, denom2)
    if denom1 != lcm_of_denoms:
        numer1 = numer1 * ( lcm_of_denoms / denom1 )
        denom1 = denom1 * ( lcm_of_denoms / denom1 )
    if denom2 != lcm_of_denoms:
        numer2 = numer2 * ( lcm_of_denoms / denom2 )
        denom2 = denom2 * ( lcm_of_denoms / denom2 )
        
    son = numer1 + numer2
    if math.gcd(int(son), lcm_of_denoms) == 1:
        return [int(son), lcm_of_denoms]  
    else:
        return [int(son) / math.gcd(int(son), lcm_of_denoms), lcm_of_denoms / math.gcd(int(son), lcm_of_denoms) ]

numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

print(solution(numer1, denom1, numer2, denom2))