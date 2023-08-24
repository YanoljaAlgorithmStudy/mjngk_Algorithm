#0824
# [3차] 방금그곡

def solution(m, musicinfos):
    answer = '(None)'
    res=[]
    for i in range(len(musicinfos)):
        arr=list(map(str, musicinfos[i].split(',')))
        
        title=arr[2]
        music=arr[3]
        
        # #처리
        d=["C#", "D#", "F#", "G#", "A#"]
        dz=["1", "2", "3", "4", "5"]
        for j in range(len(d)):
            music=music.replace(d[j], dz[j])
            m=m.replace(d[j], dz[j])
        
        # 재생시간 = 시작-종료
        start_hour, start_minute =int(arr[0][:2]), int(arr[0][3:])
        end_hour, end_minute= int(arr[1][:2]), int(arr[1][3:])
        time=(end_hour*60+end_minute)-(start_hour*60+start_minute)
        
        # 전체가사 구하기
        s=''
        k=0
        for i in range(time):
            if k==len(music):
                k=0
            s+=music[k]
            k+=1
        
        # 판별
        if m in s:
            res.append([time, title])
            
    if res:
        res.sort(reverse=True, key=lambda x:x[0])
        answer=res[0][1]
    return answer