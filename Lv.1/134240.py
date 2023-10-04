#1004
#푸드 파이트 대회
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer+=str(i)*(food[i]//2)
    k=answer[::-1] 
    answer+='0'+k
    return answer