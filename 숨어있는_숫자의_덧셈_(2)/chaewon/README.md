## 숨어있는 숫자의 덧셈

### enumerate

- 인덱스와 value를 함께 추출할 수 있음

```
for key, value in enumerate(list):
```

### 숫자인지 판별하는 방법

- 문자열과 숫자가 함꼐 연결되어 있기 때문에 `for`문을 사용하여 추출할 경우 `int` type이 아닌 `str` type으로 나오게 됨
- 즉, `str` type이지만, 실제 값은 숫자 값인 경우를 찾아내야 함

1. `string.ascii_letters`
2. 정규표현식
3. `isnumeric()`
4. 아스키코드 활용
