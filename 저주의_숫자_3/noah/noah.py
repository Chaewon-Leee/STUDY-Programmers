def solution(n):
    all_num = [i for i in range(200)]
    count = 1
    num = 1
    while num != 198:
        num = count * 3
        count += 1
        all_num.remove(num)
    num_list = all_num.copy()
    for i in num_list:
        print(i)
        if ("3" in str(i)) :
            all_num.remove(i)
        else:
            pass
    return all_num[n] 