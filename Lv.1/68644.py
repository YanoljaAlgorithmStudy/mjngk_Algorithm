#0810
# 두 개 뽑아서 더하기 

from itertools import combinations

def solution(numbers):
    answer = []
    arr=list(combinations(numbers, 2))
    for a, b in arr:
        answer.append(a+b)
    answer=list(set(answer))
    answer.sort()
    return answer