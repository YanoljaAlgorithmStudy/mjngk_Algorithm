#0808
#소수 만들기

from itertools import combinations
import math

def solution(nums):
    answer = 0
    s=[]
    
    arr=list(combinations(nums, 3))
    for i in arr:
        s.append(sum(i))
    
    for i in s:
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                answer+=1
                break
    answer=len(s)-answer
    return answer