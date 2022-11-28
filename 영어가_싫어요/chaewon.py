def solution(numbers):
    eng_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
      if eng_str[i] in numbers:
        numbers = numbers.replace(eng_str[i], str(i))
    return int(numbers)