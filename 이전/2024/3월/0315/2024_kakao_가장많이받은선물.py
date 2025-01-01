def convert_friend_idx(friends, name): # 받은 친구 이름을 인덱스로 변경해주는 함수
    idx = 0
    for i in range(len(friends)):
        if friends[i] == name:
            idx = i
            return idx


def solution(friends, gifts): # 가장 많은 선물을 받을 친구가 받을 선물의 수를 구하자
    answer = 0
    gift_dict = {} # 선물지수를 계산하기 위한 딕셔너리
    get_gift_dict = {} # 다음달에 받을 선물 수를 계산하기 위한 딕셔너리
    gift_history = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    # friends 인덱스 0에 해당하는 친구 -> 0번 인덱스
    # friends 인덱스 1에 해당하는 친구 -> 1번 인덱스
    for i in friends:
        gift_dict[i] = 0
        get_gift_dict[i] = 0
    
    for i in gifts:
        give, given = i.split()
        gift_dict[give] += 1
        gift_dict[given] -= 1 # 선물지수 체크
        gift_history[convert_friend_idx(friends, give)][convert_friend_idx(friends, given)] += 1
        # gift_hsitory[준사람][받은사람]

    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            if gift_history[i][j] > gift_history[j][i]: # i가 주고 j가 받은게 j가 주고 i가 받은 것 보다 많을 때
                # 다음번에 i가 하나 받아야 함
                get_gift_dict[friends[i]] += 1
            elif gift_history[i][j] < gift_history[j][i]:
                # 다음번에 j가 하나 받아야 함
                get_gift_dict[friends[j]] += 1
            else:
                if gift_dict[friends[i]] > gift_dict[friends[j]]:
                    # i가 하나 받음
                    get_gift_dict[friends[i]] += 1
                elif gift_dict[friends[i]] < gift_dict[friends[j]]:
                    # j가 하나 받음
                    get_gift_dict[friends[j]] += 1

    
    for i in get_gift_dict:
        if get_gift_dict[i] > answer:
            answer = get_gift_dict[i]

    return answer

# '두 사람간에'선물 주고받은 기록 바탕으로 다믕달 누가 선물 제일 많이 받을지 예측
# 선물 주고받은 기록 있음 -> 더 많이 준 사람이 다음달에 선물 하나 줌
# 주고받은 기록이 없거나 횟수가 같다 -> 선물지수 큰 사람이 작은 사람으로부터 선물 하나 받음
# 선물 지수 -> 이번달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
# 선물 지수마저 같다 -> 다음달에 선물 주고받지 않음

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"] # 앞의 친구가 뒤의 친구에게 선물을 줌

ans = solution(friends, gifts)

print(ans)