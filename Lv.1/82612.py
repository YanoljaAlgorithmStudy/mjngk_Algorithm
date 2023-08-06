# 부족한 금액 계산하기

def solution(price, money, count):
    answer = 0
    if count%2==0:
        res=(1+count)*(count//2)
    else:
        res=(1+count)*(count//2)+count//2+1
    answer=(price*res)-money
    if answer<0:
        answer=0
    return answer