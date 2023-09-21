#0922
#괄호 회전하기
def solution(s):
    answer = 0
    length=len(s)
    s=s+s
    for i in range(length):
        k=s[i:i+length]
        
        arr=[]
        for j in k:
            if j =="[" or j=="(" or j=="{":
                arr.append(j)
            elif len(arr)==0:
                arr.append(0)
                break
            elif j=="]" and (arr[-1]=="["):
                arr.pop()
            elif j==")" and (arr[-1]=="("):
                arr.pop()
            elif j=="}" and (arr[-1]=="{"):
                arr.pop()
            else:
                arr.append(j)
                break
        if len(arr)==0:
            answer+=1
    return answer
