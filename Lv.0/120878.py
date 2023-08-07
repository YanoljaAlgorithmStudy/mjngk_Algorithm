# 0808
# 유한소수 판별하기

import math

def solution(a, b):
    answer = 2
    k=math.gcd(a, b)
    b//=k
    
    while True:
        if (b%2!=0 and b%5!=0) or b==1:
            break
        if b%2==0:
            b//=2
        if b%5==0:
            b//=5
            
    if b==1:
        answer=1  
    return answer