#0914
#문자열 정수의 합

def solution(num_str):
    answer = 0
    answer=sum(list(map(int, num_str)))
    return answer