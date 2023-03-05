## 다항식 더하기

## 만약 문제가 정답 처리 되지 않을 경우, 틀린 테스트 케이스를 어떻게 확인하는가 ??

- 8, 10, 12번이 풀리지 않아 정답 처리가 되어있지 않았으며, 다른 사람이 적어놓은 계수 1일 경우, 그냥 x로 출력화는 부분이 처리되지 않아 문제였음
- 예제 조건에 맞는 생성 함수를 만들어, 문제에 맞추어 `randint()`으로 예제를 생성하는 함수와 인터넷에서 `정답 코드`를 구해 해당 정답과 틀린 `나의 코드`를 넣어 비교하는 식으로 테스트를 해보더라...

## 다른 사람의 풀이

```
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
```
