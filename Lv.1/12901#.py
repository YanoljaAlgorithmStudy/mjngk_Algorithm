#0906
# 2016년
def solution(a, b):
    day=["FRI", "SAT","SUN","MON","TUE","WED","THU"]
    thirty_one=[1,3,5,7,8,10,12]
    answer = ''
    k=0
    for i in range(1, a):
        if i in thirty_one:
            k+=31
        elif i==2:
            k+=29
        else:
            k+=30
    k+=b
    answer=day[k%7-1]
    return answer