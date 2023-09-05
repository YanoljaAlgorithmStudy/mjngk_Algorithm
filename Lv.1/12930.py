#0905
#이상한 문자 만들기

def solution(s):
    answer = ''
    li=[]
    s=list(map(str, s.split(' ')))
    print(s)
    for i in s:
        k=''
        for j in range(len(i)):
            if j%2==0:
                k+=i[j].upper()
            else:
                k+=i[j].lower()
        li.append(k)
    answer=' '.join(li)
    return answer