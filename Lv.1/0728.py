# 문자열 다루기 기본

def solution(s):
    answer = True
    if len(s)!=4 and len(s)!=6:
        answer=False
    if s.isdigit()==False:
        answer=False  

    return answer