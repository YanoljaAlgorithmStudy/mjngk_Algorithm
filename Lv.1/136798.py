#0908
# 기사단원의 무기
def solution(number, limit, power):
    answer = 0
    arr=[1]*(number)
    # 약수 배열 생성
    for i in range(2, number+1):
        j=1
        while i*j<=number:
            arr[i*j-1]+=1
            j+=1
    
    # 철 무게 계산
    for i in arr:
        if i<=limit:
            answer+=i
        else:
            answer+=power
    return answer