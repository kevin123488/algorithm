def solution(progresses, speeds):
    answer = []
    
    # 각 기능은 진도 100퍼일 때 서비스에 반영 가능
    # 기능별 개발속도 다름
    # 뒤에 있는 기능이 먼저 개발될 수도 있음. 이 때 뒤에 있는 기능 -> 앞에 기능
    # 배포될 때 같이 배포
    # 배포 작업 순서 -> progresses
    # 각 작업의 개발 속도 적힌 정수 배열 speeds
    # 각 배포마다 몇개의 기능이 배포되는지 구해야 함
    
    # 배포는 하루에 한 번, 하루의 끝에 진행
    # 진행도는 93, 30, 55, 각 작업별 속도는 1, 30, 5
    # 첫날 끝 -> 94, 60, 60
    # 둘째날 끝 -> 95, 90, 65
    # 셋째날 끝 -> 96, 120(배포가능), 70
    
    # 로직
    # 가장 앞에 있는 작업이 100퍼가 되는 날을 기준으로 첫째 배포날 카운트 실행
    # 앞 작업이 모두 완성되어야 배포가 가능함
    # 스택 활용
    
    day = 1
    finish_cnt = 0
    while True:
        temp = []
        for i in range(len(progresses)):
            progress_after_day = progresses[i] + day*speeds[i] # n일이 지난 후 해당 프로젝트의 진행도
            if progress_after_day >= 100 and finish_cnt == i:
                # 특정 과제에 대해서
                # 해당 과제의 진행도가 100퍼센트를 달성하고
                # 이전에 달성한 과제의 수가 해당 과제의 인덱스와 같을 경우 해당 과제 배포(temp 리스트에 넣어줌)
                
                temp.append(i)
                finish_cnt += 1
        
        day += 1
        if len(temp) == 0:
            continue
        else:
            answer.append(len(temp))
        
        if sum(answer) == len(progresses):
            break
                
            
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))