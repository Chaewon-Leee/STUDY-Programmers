def solution(id_pw, db):
    id, pw = id_pw
    for db_id, db_pw in db:
        if id == db_id:
            if pw == db_pw:
                result = "login"
                break
            else:
                result = "wrong pw"
                break
        else:
            result = "fail"
    return result
id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
print(solution(id_pw, db))
