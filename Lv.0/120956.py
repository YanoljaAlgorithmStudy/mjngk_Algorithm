# 0807
# 옹알이 (1)

def solution(babbling):
    answer = 0
    arr=["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in arr:
            if j in i:
                i=i.replace(j, " ")
                print(i)
        if len(i.replace(" ", ""))==0:
            answer+=1
    return answer