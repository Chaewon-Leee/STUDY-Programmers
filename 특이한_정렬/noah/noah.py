def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : abs(x-n))
    answer_copy = answer.copy()
    for i in answer_copy:
        if i-n < 0 :
            if abs(i-n)+ n in answer :
                a = answer.index(n-abs(i-n))
                b = answer.index(abs(i-n)+ n)
                if a < b:
                    print("swap", i)
                    answer[a], answer[b] = answer[b], answer[a]
            else:
                pass

    return answer

# 다른 풀이
def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n),n-x))
    # answer = sorted(numlist,key = lambda x : (abs(x-n), n-x)) key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다.
    # 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다.
    # 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열되는 것 같다(인덱스가 작은 것이).
    return answer

numlist =  [10000,20,36,47,40,6,10,7000]
n = 30
print(solution(numlist, n))