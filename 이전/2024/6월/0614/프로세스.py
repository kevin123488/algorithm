def solution(priorities, location):
    answer = 0
    # 큐에서 대기중인 프로세스 하나 꺼냄
    # 큐에 대기중인 프로세스 중 우선순위 더 높은 프로세스 있다
    # -> 꺼낸거 다시 큐에 넣음
    # 없다?
    # -> 꺼낸거 실행
    # 실행된건 큐에 안넣고 종료
    
    # 해시로 일단 프로세스와 우선순위를 저장하자
    priorities_2 = [0] * len(priorities)
    for i in range(len(priorities)):
        priorities_2[i] = [priorities[i], i]
    
    # print(priorities_2)
    q = sorted(priorities, reverse = True)
    # print(q)
    # 큐에서 꺼낸 수가 큐에 남아있던 수 중 가장 크다면 실행
    while True:
        if priorities_2[0][0] == q[0]:
            q = q[1:]
            answer += 1
            if priorities_2[0][1] == location:
                return answer
            priorities_2 = priorities_2[1:]
        else:
            priorities_2 = priorities_2[1:] + [priorities_2[0]]
    
    
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))