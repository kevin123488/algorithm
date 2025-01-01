def check_ans(answer, diffs, times, limit):
    n = len(diffs)
    check_limit = 0
    for i in range(n):
        if answer >= diffs[i]:
            check_limit += times[i]
        else:
            if i == 0:
                check_limit += (diffs[i] - answer) * times[i]
            else:
                check_limit += (times[i - 1] + times[i]) * (diffs[i] - answer)
            check_limit += times[i]
        # if check_limit > limit:
        #     return False
    
    if check_limit <= limit:
        return 1
    else:
        return 0

def solution(diffs, times, limit):
    answer = 0
    
    # n개의 퍼즐 시간 내에 풀어야 함
    # 퍼즐당 난이도와 소요 시간이 있음
    # 현 퍼즐 난이도: diff, 현 퍼즐 소요 시간: time_cur,
    # 전 퍼즐 소요 시간: time_prev, 숙련도: level
    # 내 수준이 현 퍼즐 난이도 이상이다 -> 안틀리고 time_cur 시간 써서 해결
    # 난이도가 내 수준 초과다 -> 퍼즐을 난이도 - 숙련도의 횟수 만큼 틀림
    # 퍼즐 틀릴 때 마다 time_cur 만큼의 시간을 씀, time_prev 만큼의 시간을 써서 이전 퍼즐 풀어야 함
    # 이전 퍼즐을 풀 땐 틀리지 않음
    # 난이도 - 숙련도 횟수 만큼 틀린 후 다시 퍼즐을 풀면 time_cur 만큼 시간 써서 문제 해결
    # 요약: 숙련도가 난이도 이상이다 -> time_cur
    # 숙련도가 난이도 초과다 -> (time_cur + time_prev) * (diff - level) + time_cur
    # 주어진 시간 limit 안에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하기
    
    # 간단히 생각하면 level을 1부터 1씩 올려가며 시간 내에 모든 문제를 해결할 수 있는
    # 최솟값을 구하면 됨
    # 그러나 그렇게 하면 시간이 오버될 것. 여기선 수학적으로 푸는게 맞는 것 같다
    # 일단 level의 범위는 1 ~ max(diffs)
    # 이분탐색을 사용하는게 좋을듯. 시작은 max(diffs) 일 때, 리밋 이내로 풀리면 max(diffs) // 2
    
    start = 1
    end = max(diffs)
    
    # limit 내로 풀리면 answer를 절반씩 줄여가며 계산
    # 탐색 대상이 7
    # 시작 answer가 20, end가 20, start가 1
    # start, answer, end
    # 1, 10, 20
    # 1, 5, 10
    # 5, 7, 10
    
    while start <= end:
        semi_answer = (start + end) // 2
        if check_ans(semi_answer, diffs, times, limit) == 1: # 지금 level로 limit 내의 시간에
            # 문제를 다 풀 수 있다면
            end = semi_answer - 1
            answer = semi_answer
        else:
            # 지금 level로 문제 다 못풀면
            start = semi_answer + 1
    
    return answer