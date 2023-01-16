def solution(sides):
    a, b = sorted(sides)
    # b가 제일 길 경우
    answer = a
    # 나머지 한 변이 가장 길 경우
    answer += (a+b-1)-(b+1)+1
    return answer

sides = [1, 2]
print(solution(sides))