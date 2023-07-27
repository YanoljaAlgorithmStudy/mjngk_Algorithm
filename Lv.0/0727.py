# 문자열 계산하기
def solution(my_string):
    arr=list(map(str, my_string.split(" ")))
    answer = int(arr[0])
    
    for i in range(1, len(arr)-1):
        if arr[i]=="+":
            answer+=int(arr[i+1])
        elif arr[i]=="-":
            answer-=int(arr[i+1])
    return answer
