#0921
#정수 삼각형

def solution(triangle):
    answer = 0
    length=len(triangle)
    dp=[[0]*(length) for _ in range(length)]
    dp[0][0]=triangle[0][0]

    for i in range(1, length):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][0]+triangle[i][0]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
    # print(dp)
    return max(dp[length-1])