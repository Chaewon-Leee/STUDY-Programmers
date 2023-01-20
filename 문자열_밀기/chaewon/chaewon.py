def solution(A, B):
    answer = 0
    new_word = A
    num = len(A)
    count = len(A)

    while count != 0:
      if new_word == B:
        break
      else:
        new_word = A[num -1] + A[:num -1]
        A = new_word
        answer += 1
      count -= 1

    if answer == len(A):
      answer = -1

    return answer

# print(solution("abc", "abc"))
print(solution("apple", "elppa"))