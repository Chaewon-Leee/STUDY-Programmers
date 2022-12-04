def solution(my_string):
    for i in my_string:
      if 65 <= ord(i) <= 122: my_string = my_string.replace(i, " ")
    return sum(map(int, my_string.split()))