def solution(numbers, k):
    new_numbers = numbers * k
    target_index = (2*k-2)
    for i, new_numbers in enumerate(new_numbers):
        if i == target_index:
            answer = new_numbers
    return answer