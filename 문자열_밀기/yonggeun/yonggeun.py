def solution(A, B):
    a_list = list(A)
    b_list = list(B)
    if A == B:
        return 0
    for i in range(len(A)):
        a_list.insert(0, a_list.pop())
        if a_list == b_list:
            return i + 1
    return -1


A = "atat"
B = "tata"
print(solution(A, B))

# "hello"	"ohell"	
# "apple"	"elppa"	
# "atat"	"tata"
# "abc"	"abc"