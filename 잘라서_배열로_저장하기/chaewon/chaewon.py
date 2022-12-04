def solution(my_str, n):
    import math
    return [my_str[i*n:(i+1)*n] for i in range(math.ceil(len(my_str)/n))]