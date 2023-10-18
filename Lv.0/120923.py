#1018
#연속된 수의 합
def solution(num, total):
    answer = []
    start=total//num-(num-1)//2
    
    for i in range(num):
        answer.append(start+i)
    return answer