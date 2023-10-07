#1007
#다음 큰 숫자
def solution(n):
    answer = 0
    cnt=bin(n).count('1')
    print('n:',n,',  cnt', cnt)
    
    for i in range(n+1, 1000001):
        k=bin(i).count("1")
        if cnt==k:
            answer=i
            break
    print(n)
    return answer