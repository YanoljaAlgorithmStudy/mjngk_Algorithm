def solution(array):
    answer = 0
    arr=[0] * (max(array)+1)
    
    for i in array:
        arr[i]+=1
    
    maxi=0
    for j in arr:
        if j==max(arr):
            maxi+=1
            
    if maxi>1:
        answer-=1
    else:
        answer=arr.index(max(arr))
    return answer