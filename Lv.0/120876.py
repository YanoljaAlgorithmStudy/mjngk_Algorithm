#0916
#겹치는 선분의 길이
def solution(lines):
    answer = 0
    arr={}
    for a, b in lines:
        for i in range(a, b):
            if i in arr:
                arr[i]='2'
            else:
                arr[i]='1'
    for i in arr:
        if arr[i]=="2":
            answer+=1
    return answer