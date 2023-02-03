def solution(numlist, n):
    answer = []

    distance = list(map(lambda x: abs(x - n), numlist))
    for i in sorted(distance):
        answer.append(numlist[distance.index(i)])
    visited = set()
    dup = [x for x in answer if x in visited or (visited.add(x) or False)]
    for i in dup:
        if i < n:
            answer[answer.index(i)] = i - 2*(i-n)
        else:
            answer[answer.index(i) + 1] = i - 2*(i-n)
    return answer

numlist = [600, 400, 300, 200, 700, 800, 100, 900]
n = 500

print(solution(numlist, n))


# def solution(numlist, n):
#     answer = []
#     distance = []
#     for i, num in enumerate(numlist):
#         distance.append([i,abs(num - n)])
#     distance.sort(key=lambda x: x[1])
#     # print(distance)
#     for idx, dis in distance:
#         answer.append(numlist[idx])
#     return answer