def solution(id_pw, db):
    result = "fail"

    for _id, pw in db:
      if _id == id_pw[0]:
        if pw == id_pw[1]:
          result = "login"
        else:
          result = "wrong pw"

    return result

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))