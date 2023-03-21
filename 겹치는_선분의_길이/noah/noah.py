def fillnum(list):
    a, b = list
    result = []
    while a != b:
        result.append(a)
        a += 1
    return result

def solution(lines):
    # 리스트 빈값 채워주기
    fir, sec, thi = sorted(lines)
    fir, sec, thi = fillnum(fir), fillnum(sec), fillnum(thi)
    # 교집합 구하기
    return len(list((set(fir)&set(sec)) | set(thi)&set(sec) | set(fir)&set(thi)))





lines = [[-1, 4], [1, 3], [3, 9]]
print(solution(lines))