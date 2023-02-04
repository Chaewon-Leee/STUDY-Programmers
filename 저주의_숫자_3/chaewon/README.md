## 저주의 숫자 3

```
def solution(n):
    answer = 0

    i = 1
    while n:
        if i % 3 and '3' not in str(i):
            n -= 1
        i += 1
    answer = i - 1
```
