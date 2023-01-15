def solution(sides):
    maxIsHere = [i for i in range(max(sides)-min(sides),max(sides))]
    maxIsNew = [i for i in range(max(sides)+1,max(sides)+min(sides))]
    answer = len(maxIsHere + maxIsNew)
    return answer