def solution(n):
    num_list = []
    num = 1
    
    while len(num_list) <= 100:
        if num%3 != 0 and "3" not in str(num):
            num_list.append(num)
        num += 1
        
    return num_list[n-1]