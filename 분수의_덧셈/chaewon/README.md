## 분수의 덧셈

```
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
```

```
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer
```
