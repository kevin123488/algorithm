def solution(brown, yellow):
    answer = []
    
    # 테두리 -> 갈색
    # 그 외 -> 노란색
    # 갈색 수와 노란색 수 주어질 때 해당 카펫의 가로, 세로 길이를 리스트에 담아 리턴
    
    # 갈색 + 노란색 -> 전체
    # 방정식 풀자
    # 가로 * 세로 = 갈색 + 노랑
    # (가로 - 2) * (세로 - 2) = 노랑
    # 가로 * 세로 = 갈색 + (가로 - 2) * (세로 - 2)
    # 0 = 갈색 - 2*가로 -2*세로 + 4
    # 가로 + 세로 = (갈색 + 4) / 2
    
    garo_sero_sum = int((brown + 4) / 2) # 가로 + 세로
    for i in range(1, garo_sero_sum):
        sero = i
        garo = garo_sero_sum - i
        if garo * sero == brown + yellow:
            answer = [garo, sero]
            break
    
    return answer

brown = 8
yellow = 1
print(solution(brown, yellow))