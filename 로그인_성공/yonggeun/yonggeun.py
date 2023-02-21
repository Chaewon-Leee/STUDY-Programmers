def solution(id_pw, db):
    for user in db:
        if user[0] == id_pw[0]:
            if user[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
print(solution(id_pw, db))