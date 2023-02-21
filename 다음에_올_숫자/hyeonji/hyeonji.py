def solution(common):
    # 제한사항 1
    # 2 < common의 길이 < 1000
    if 2 < len(common) < 1000 :
        # 제한사항 2
        # -1,000 < common의 원소 < 2,000
        common = [i for i in common if -1000 < i < 2000]
    
    first, second, third = common[:3]
    
    # 등차수열
    if (second - first) == (third - second) :
        answer = common[-1] + (third - second)
    # 등비수열
    elif (second // first) == (third // second) : 
        answer = common[-1] * (third // second)
    return answer