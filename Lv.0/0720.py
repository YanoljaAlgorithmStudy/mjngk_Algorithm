#구슬을 나누는 경우의 수
import math

def solution(balls, share):
    answer = 0
    answer=math.comb(balls, share)
    return answer