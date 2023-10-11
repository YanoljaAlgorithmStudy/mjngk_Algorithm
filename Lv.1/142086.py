#1011
#가장 가까운 글자
def solution(s):
    answer = []
    stack=[0]*26
    for i in range(len(s)):
        k=stack[ord(s[i])-97]
        # print(s[i], ord(s[i])-97, k)
        if k==0:
            answer.append(-1)
        else:
            answer.append(i-k+1)
        stack[ord(s[i])-97]=i+1
    return answer