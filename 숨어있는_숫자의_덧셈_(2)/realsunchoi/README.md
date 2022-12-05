## 숨어있는 숫자의 덧셈

### 코드 설명

1. 주어진 문자열 `my_string`을 사용하여 for문을 돈다

   ⅰ) i가 숫자이면 -> 문자열 `my_number`에 i를 더함

   ⅱ) i가 문자이면 -> 이때까지 저장된 `my_number`을 `number`배열에 append

2. for문을 다 돌고 나면 `number` 배열을 돌면서 얻은 숫자들의 합을 구하여 `answer`로 return한다.

### 관련 이슈

1. 문자열이 숫자인지 판별하는 방법

   `isnumeric()` 사용
