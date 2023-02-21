def solution(array):
    
    result = []
    number = []
    
    for value in array :
        if value not in result :
            result.append(value)
    
    for i in result :
        num = array.count(i)
        number.append(num)
        
    max_count = number.count(max(number)) 

    if (len(number) > 1) & (max_count > 1) :
        answer = -1
        
    else :
        index = result.index(max(number))
        answer = result[index]
        
    return answer