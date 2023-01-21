## 소인수분해

### 리스트 중복 제거

- `set`으로 변환시 중복을 제거하여 반환해줌
- 이후, 리스트로 다시 타입 변환

```
list(set(answer))
```

### 소수랑 약수 구분 함수를 따로 짜는 것

- 약수를 for문을 2개 사용하지 않고 하는 법

```
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
```

-> 노아오빠꺼랑 비슷한듯
