#1012
#점프와 순간 이동
def solution(n):
    ans = 0
    
    while True:
        if n==0:
            break
        if n%2==0:
            n//=2
        else:
            n-=1
            ans+=1
    return ans


# def solution(n):
#     ans =  1
#     dp=[0]*(n+4)
    
#     dp[0]=0
#     dp[1]=1
#     for i in range(2, n+1):
#         if i%2==0:
#             dp[i]=min(dp[i-1]+1, dp[i//2])            
#         else:
#             dp[i]=dp[i-1]+1
#     ans=dp[n]
#     return ans