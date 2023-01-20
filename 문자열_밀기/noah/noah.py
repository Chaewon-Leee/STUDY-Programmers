def solution(A, B):
    list_A = list(A)
    if A == B:
        return 0
    else:
        for i in range(len(list_A)):
            last_str = list_A.pop()
            list_A.insert(0, last_str)
            if B == "".join(list_A):
                return  i+1
            else:
                answer = -1
    return answer 
A = "hello"
B = "llohe"

print(solution(A,B))