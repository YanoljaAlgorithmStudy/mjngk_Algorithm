#1005
#코드 처리하기

def solution(code):
    answer = ''
    mode=0
    for i in range(len(code)):
        if mode==0:
            if code[i]=="1":
                mode=1
            elif i%2==0:
                answer+=code[i]
        else:
            if code[i]=="1":
                mode=0
            elif i%2!=0:
                answer+=code[i]
    if len(answer)==0:
        answer="EMPTY"
    return answer