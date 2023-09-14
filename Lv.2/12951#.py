# 0915
# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    arr=list(map(str, s.split(" ")))
    for i in range(len(arr)):
        if arr[i]!="":
            arr[i]=arr[i].lower()
            arr[i]=str(arr[i][0]).upper()+arr[i][1:]
    # print(arr)
    answer=" ".join(arr)
    return answer