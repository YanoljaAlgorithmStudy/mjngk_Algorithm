#0809
# 조건 문자열

def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq=='>':
        if eq=="=" and n>=m:
            answer=1
        elif eq=="!" and n>m:
            answer=1
            
    else:
        if eq=="=" and n<=m:
            answer=1
        elif eq=="!" and n<m:
            answer=1
    return answer