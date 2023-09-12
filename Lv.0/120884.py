#0912
#치킨쿠폰 

def solution(chicken):
    answer = 0
    while True:
        k=chicken//10
        chicken%=10
        chicken+=k
        answer+=k
        if chicken<10:
            break
    return answer