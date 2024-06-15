def truck_can(now_bridge, weight, i): # 도로 상황을 체크, 새 차량을 올릴 수 있으면 true, 불가능이면 false 반환
    weight_sum = i
    for j in now_bridge:
        weight_sum += j[0]
    
    if weight_sum > weight:
        return False
    else:
        return True

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭 여러대가 일차선 다리 정해진 순으로 건넘
    # 모든 트럭이 건너는데 몇 초가 걸리는지 (최소로)
    # 다리에는 트럭이 최대 bridge_length대 만큼 올라갈 수 있음
    # 다리는 weight 이하까지의 무게 견딜 수 있음
    # 다리에 완전히 오르지 않은 트럭의 무게는 무시
    # 한 대가 지나는데 bridge_length초 만큼 걸림
    
    now_bridge = [] # 현재 다리를 건너고 있는 트럭
    # 위에 넣을 때 다리에 올라선지 몇 초가 지났는지 카운트 해 줄 필요 있음
    # [[4, 2], [5, 1]]
    
    now_weight = 0 # 현재 다리 위에 올라와있는 차량의 무게 합
    
    # 주의사항: length가 2인 도로를 건너는데 걸리는 시간 -> 3초
    # [[], []] -> 이걸 도로라고 하자
    # [[], []] -> 0초
    # [[a], []] -> 1초
    # [[], [a]] -> 2초
    # [[], []] -> 3초
    
    # for i in range(len(truck_weights)):
    i = 0
    while i < len(truck_weights):
        now_truck = truck_weights[i]
        answer += 1
        # 도로가 비어있지 않다면 차량을 전진 시켜줘야 함
        if len(now_bridge) != 0:
            for j in range(len(now_bridge)):
                now_bridge[j] = [now_bridge[j][0], now_bridge[j][1] + 1] # 도로위에 올라가있는 시간 갱신
                
            # 내릴 차량 내려주기
            if now_bridge[0][1] == bridge_length + 1:
                now_bridge = now_bridge[1:]
            
        # 도로의 상황을 체크하고 추가로 올릴 수 있는지 없는지 확인
        # print('차량 올리기 전', now_bridge, now_truck)
        if truck_can(now_bridge, weight, now_truck):
            i += 1
            # 도로에 차량을 올리자
            now_bridge.append([now_truck, 1]) # 도로에 처음 올릴 땐 1초로 카운트. [무게, 올라오고 나서 지난 시간]
        # else:
        #     print('hi')
        
        # print('차량 올린 후', now_bridge)
            
    # 위의 for문 다 돌면 도로에 남아있는 트럭이 나올 것
    # 가장 끝에 있는 트럭이 도로를 통과하는데 걸리는 시간 계산해서 answer에 더해주자
    
    answer += (bridge_length - now_bridge[-1][1] + 1)
    
    return answer

bridge_length, weight, truck_weights = 2, 10, [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))