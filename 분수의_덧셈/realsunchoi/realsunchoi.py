def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    num = 2
    while num <= min(numer, denom):
        if numer % num == 0 and denom % num == 0:
            numer = numer / num
            denom = denom / num
        else:
            num += 1
            
    return [numer, denom]