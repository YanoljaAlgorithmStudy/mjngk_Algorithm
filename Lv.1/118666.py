#0907
#성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    # print(survey)
    # print(choices)
    arr=["R", "T", "C", "F", "J", "M", "A", "N"]
    arr2=[0]*8
    
    for i in range(len(survey)):
        score=choices[i]-4
        x=survey[i][0]
        y=survey[i][1]        
        if score<0:
            arr2[arr.index(x)]+=abs(score)
        else:
            arr2[arr.index(y)]+=score
            
    for i in range(len(arr)//2):
        if arr2[i*2]==arr2[i*2+1]:
            answer+=str(min(arr[i*2], arr[i*2+1]))
        elif arr2[i*2]>arr2[i*2+1]:
            answer+=str(arr[i*2])
        else:
            answer+=str(arr[i*2+1])
        
    # print(arr)
    # print(arr2)
    return answer