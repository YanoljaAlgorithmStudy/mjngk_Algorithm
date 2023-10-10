#1010
#짝지어 제거하기

def solution(s):
    answer = 0
    stack=[]
    
    for i in range(len(s)):
        if len(stack)==0:
            stack.append(s[i])
        elif stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack)==0:
        answer=1

    return answer

# def solution(s):
#     answer,i = 0,0
#     print(s)
#     while True:
#         if i==len(s) or len(s)==0:
#             # print(s)
#             break
#         if s[i-1]==s[i]:
#             s=s[:i-1]+s[i+1:]
#             i=0
#         i+=1
#     if len(s)==0:
#         answer=1
#     else:
#         answer=0
#     return answer