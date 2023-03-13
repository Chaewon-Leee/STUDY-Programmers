def solution(polynomial):
    answer = ''
    split_polynomial = polynomial.split(" ")
    coefficient_term = 0
    consistant_term = 0

    for idx, char in enumerate(split_polynomial):
      if (idx%2 == 0) and (char != "+"):
        isvariable = char[-1]
        ## 숫자인 경우
        if isvariable.isnumeric() is True:
          consistant_term += int(char)
        ## 숫자가 아닐 경우 = 변수일 경우
        else:
          if len(char) == 1:
            coefficient = 1
          else:
            coefficient = int(char[:-1])
          coefficient_term += coefficient

    if not coefficient_term == 0:
      ## 걔수가 1인 경우, 생력
      if coefficient_term == 1:
        answer += f"x"
      else:
        answer += f"{str(coefficient_term)}x"

      if not consistant_term == 0:
        answer += f" + {str(consistant_term)}"

    else: ## coefficient_term == 0
      answer += f"{str(consistant_term)}"

    return answer