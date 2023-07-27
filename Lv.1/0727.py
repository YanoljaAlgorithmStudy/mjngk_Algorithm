# 숫자 문자열과 영단어

def solution(s):
    answer = 0
    arr=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if s.isdigit()==True:
        answer=int(s)
    else:
        for i in arr:
            if i in s:
                s=s.replace(i, str(arr.index(i)))
                print(arr.index(i), s)
                
    answer=int(s)
    return answer