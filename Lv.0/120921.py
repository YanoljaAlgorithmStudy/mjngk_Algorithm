# 문자열 밀기

def solution(a, b):
    answer = 0
    k=a    
    while True:
        if answer>=100:
            answer=-1
            break
        if k==b:
            break
        else:
            k=k[-1]+k[:-1]
            answer+=1
    return answer








# def solution(A, B):
#     answer = -1
#     cnt=0
#     A=list(A)
#     B=list(B)
    
#     while True:
#         if A==B:
#             if cnt==0:
#                 return 0
#             return cnt
#         if cnt==len(A):
#             return answer
#         C=A.pop()
#         A.insert(0, C)
#         cnt+=1