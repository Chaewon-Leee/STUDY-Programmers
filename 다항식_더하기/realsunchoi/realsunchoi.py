def solution(polynomial):
    linear = 0
    constant = 0
    before_cal = polynomial.replace("+ ", "").split()

    for i in before_cal:
        if i[-1] == "x":
            if i[:-1] != "":
                linear += int(i[:-1])
            else:
                linear += 1
        else:
            constant += int(i)

    if linear == 0:
        return str(constant)
    elif linear == 1:
        if constant == 0:
            return "x"
        else:
            return "x + " + str(constant)
    else:
        if constant == 0:
            return str(linear) + "x"
        else:
            return str(linear) + "x + " + str(constant)

