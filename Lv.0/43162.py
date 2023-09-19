#0919
#OX퀴즈
def solution(quiz):
    answer = []
    for i in quiz:
        arr=list(i.split(" "))
        if arr[1]=='-':
            k=int(arr[0])-int(arr[2])
        elif arr[1]=='+':
            k=int(arr[0])+int(arr[2])
        if k==int(arr[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer