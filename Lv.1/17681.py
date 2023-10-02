#1002
#[1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a,b = bin(arr1[i])[2:], bin(arr2[i])[2:]
        if n-len(a)!=0:
            a='0'*(n-len(a))+a
        if n-len(b)!=0:
            b='0'*(n-len(b))+b
        k=''
        for j in range(n):
            if a[j]=='0' and b[j]=='0':
                k+=' '
            else:
                k+='#'
        answer.append(k)
    return answer