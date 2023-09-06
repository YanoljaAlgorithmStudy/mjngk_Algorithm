#0907
# 소수 찾기

import math

def solution(n):
    answer = 0
    arr=[1]*(n+1)
    
    for i in range(2, int(math.sqrt(n)+1)):
        j=2
        while i*j<=n:
            arr[i*j]=0
            j+=1
    # print(arr)
    answer=sum(arr)-2
    return answer