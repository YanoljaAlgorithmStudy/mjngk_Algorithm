#0809
#모의고사

def solution(answers):
    answer = []
    a=[1, 2, 3, 4, 5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1=0
    b1=0
    c1=0
    
    for i in range(len(answers)):
        if answers[i]==a[i%5]:
            a1+=1
        if answers[i]==b[i%8]:
            b1+=1
        if answers[i]==c[i%10]:
            c1+=1
            
    maxi=max(a1,b1,c1)
    if maxi==a1:
        answer.append(1)
    if maxi==b1:
        answer.append(2)
    if maxi==c1:
        answer.append(3)
    return answer