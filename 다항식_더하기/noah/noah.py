def solution(polynomial):
    x_value, num = 0, 0
    split_poly = polynomial.split("+")
    for i in split_poly:
        i = i.strip()
        if "x" in i:
            if i == "x":
                x_value += 1
            else:
                x_value += int(i.strip("x"))
        else:
            num += int(i)
    if x_value == 1:
        x_value = ''
    if num == 0 :
        return str(f'{x_value}x')
    elif x_value == 0:
        return str(num)
    else: 
        return  str(f'{x_value}x + {num}')

polynomial = " x + x "
print(solution(polynomial))