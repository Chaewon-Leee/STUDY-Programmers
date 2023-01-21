def solution(s):
    list = s.split()
    while( "Z" in list ):
        list.pop(list.index("Z")-1)
        list.pop(list.index("Z"))

    return sum(map(int, list))

s = "10 Z 20 Z"
print(solution(s))