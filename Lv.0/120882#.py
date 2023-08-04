# 0805 등수 매기기

def solution(score):
    answer = [0]*len(score)
    i=0
    for a, b in score:
        score[i]=(a+b)/2
        i+=1
    print(score)
    
    k=1
    while True:
        if k==len(score)+1:
            break
        maxi=max(score)
        a=0
        for i in range(len(score)):
            if score[i]==maxi:
                answer[i]=k
                score[i]=-1
                a+=1
        k+=a
    return answer
