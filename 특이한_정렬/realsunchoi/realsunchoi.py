def solution(numlist, n):
    num_dict = [(abs(num-n), -num) for num in numlist]
    answer = [-(num[1]) for num in sorted(num_dict)]
    return answer