# 삼각형의 완성조건 (2)

def solution(sides):
    answer = 0
    maxi=max(sides)
    mini=min(sides)
    for i in range(1, maxi+1):
        if maxi-mini<i:
            answer+=1
    for i in range(maxi, maxi+mini+1):
        if maxi<i<maxi+mini:
            answer+=1
    return answer