#0923
#영어 끝말잇기
def solution(n, words):
    answer = []
    arr=[]
    k=0
    for i in words:
        k+=1
        if len(arr)==0:
            arr.append(i)
        elif i in arr:
            break
        elif arr[-1][-1]==i[0]:
            arr.append(i)
        else:
            break
    if len(words)==len(arr):
        answer=[0,0]
    else:
        answer=[(k-1)%n+1, (k-1)//n+1]
    return answer