# 로그인 성공?

def solution(id_pw, db):
    answer = 'fail'
    id=id_pw[0]
    pw=id_pw[1]
    for i, j in db:
        if i==id:
            if j==pw:
                answer='login'
                break
            else:
                answer='wrong pw'
                break
        
    return answer