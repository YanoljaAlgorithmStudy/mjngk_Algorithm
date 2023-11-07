#1107
# 연속 부분 수열 합의 개수
def solution(elements):
    answer = 0
    n=len(elements)
    elements*=2
    arr=[]
    sumi=0
    for i in range(1, n+1):
        for j in range(n):
            # for k in range(j, j+i):
            #     sumi+=elements[k]
            sumi=sum(elements[j:j+i])
            arr.append(sumi)
            sumi=0
            
    # print(sorted(set(arr)))
    answer=len(set(arr))
    return answer