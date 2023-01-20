def solution(A, B):
    length = len(A)
    word_list = [A]
    for i in range(length-1):
        A = (A[length-1] + A)[:length]
        word_list.append(A)
    if B in word_list:
        return word_list.index(B)
    else:
        return -1