#0906
#3진법 뒤집기

def solution(n):
    answer = 0
    s=''
    k=0
    while True:
        s+=str(n%3)
        n//=3
        if 0<n<3:
            s+=str(n)
            break
        if n<1:
            break
    s=list(map(int, s))
    while s:
        answer+=s.pop()*(3**k)
        k+=1
        
    print(s, k, answer)
    return answer