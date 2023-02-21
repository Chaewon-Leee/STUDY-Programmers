def solution(common):
    if common[2] - common[1] == common[1] - common[0]: # 등차수열인 경우
        return common[0] + ((common[1] - common[0]) * len(common))  # 초항 + (등차 * 수열의 길이)
    else:  # 등비수열인 경우
        return common[0] * ((common[1] // common[0]) ** len(common))  # 초항 x (등차 ^ 수열의 길이)      

common = [2,4,8]
print(solution(common))