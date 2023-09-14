#0915
#시저 암호

def solution(s, n):
    answer = ''
    # print(ord("a"),"-", ord("z"), "/", ord("A"),"-", ord("Z"))
    for i in s:
        k=ord(i)+n
        if i==" ":
            answer+=" "
            continue
        elif k>122:
            answer+=chr(k-26)
        elif k>90 and ord(i)<=90: 
            answer+=chr(k-26)
        else:
            answer+=chr(k)
    return answer