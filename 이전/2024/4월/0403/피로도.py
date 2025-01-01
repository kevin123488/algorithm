from itertools import permutations

def solution(k, dungeons):
    answer = -1
    all_list = [i for i in range(len(dungeons))]
    test_list = list(permutations(all_list, len(dungeons)))
    
    for i in test_list:
        # i는 테스트 종류
        tmp = k
        ans = 0
        for j in i: # j는 탐방할 던전의 인덱스
            if tmp - dungeons[j][0] >= 0:
                tmp -= dungeons[j][1]
                ans += 1
        answer = max(answer, ans)
    
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))