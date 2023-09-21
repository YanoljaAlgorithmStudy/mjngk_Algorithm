#0922
#이진 변환 반복하기
def solution(s):
    answer = []
    remove, cnt=0,0
    while True:
        length=len(s)
        if str(s)=="1":
            break
        s=len(str(s).replace("0", ""))
        remove+=length-s
        cnt+=1
        s=bin(s)[2:]
    answer=[cnt, remove]
    return answer