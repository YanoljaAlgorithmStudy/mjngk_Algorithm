# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        for j in range(n):
            answer+=i
    return answer