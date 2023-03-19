from itertools import combinations

def get_intersection(lines):
    length = 0
    intersection = []
    combination = list(combinations(lines, 2))
    
    for comb in combination:
        left = min(comb)
        right = max(comb)
    
        if not left[1] <= right[0]: # 겹치는 구간이 있을 때
            if (left[0] <= right[0]) and (left[1] >= right[1]): # right가 left의 부분집합일 때
                intersection.append(right)
                length += right[1] - right[0]
            else: # 교집합 계산
                intersection.append([right[0], left[1]])
                length += left[1] - right[0]
                
    return intersection, length

def solution(lines):
    answer = get_intersection(lines)
    intersection = answer[0]
    length = answer[1]
    result_intersection = get_intersection(intersection)
    
    if len(intersection) == 0: # lines 사이에 겹치는 구간이 없을 때
        return 0
    elif len(result_intersection[0]) == 0: # 교집합 사이에 겹치는 구간이 없을 때
        return length
    elif len(result_intersection[0]) != 3: # 교집합 사이에 겹치는 구간이 있을 때
        return length - result_intersection[1]
    else: # 똑같은 구간이 동시에 겹칠 때
        return length - (result_intersection[1]/3)*2