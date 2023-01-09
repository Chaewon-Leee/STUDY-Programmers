def solution(balls, share):
    difference = balls - share

    n = 1
    while balls != 0:
        n = n * balls
        balls -= 1
    
    m = 1
    while share != 0:
        m = m * share
        share -= 1 
    
    k = 1
    while difference != 0:
        k = k * difference
        difference -= 1
    return n // (m * k)

print(solution(5,3))