# 올바른 괄호

def solution(s):
    answer = True
    k=0
    for i in s:
        if i=="(":
            k+=1
        else:
            k-=1
            if k<0:
                break
    if k==0:
        return True
    else:
        return False