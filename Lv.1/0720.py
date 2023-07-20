# 최대공약수와 최소공배수
import math

def solution(n, m):
    answer = []
    gcd=math.gcd(n,m)
    answer.append(gcd)
    lcd=(n//gcd)*(m//gcd)*gcd
    answer.append(lcd)
    return answer