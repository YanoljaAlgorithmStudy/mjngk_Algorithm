# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    strings.sort(key=lambda x:(x[n], x))
    answer=strings
    return answer