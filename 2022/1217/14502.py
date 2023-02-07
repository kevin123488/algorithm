from itertools import permutations, combinations
from copy import deepcopy
import sys
sys.stdin = open('14502input.txt')
sys.setrecursionlimit(1000000)

# 델타탐색
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def make_cho():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt_arr.append([i, j])

def delta_find(i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and test_arr[ni][nj] == 0:
            test_arr[ni][nj] = 2
            delta_find(ni, nj)

def find_cnt():
    # arr의 바이러스를 쭉 퍼뜨리자
    cnt = 0
    virus_list = []
    for i in range(N):
        for j in range(M):
            if test_arr[i][j] == 2: # 바이러스
                virus_list.append([i, j]) # 탐색을 시작할 바이러스 리스트를 만드는 과정

    for i in virus_list:
        delta_find(i[0], i[1])

    for i in range(N):
        for j in range(M):
            if test_arr[i][j] == 0:
                cnt += 1

    return cnt

# 크기 N * M인 연구소
# 일부 칸은 바이러스가 존재, 상하좌우 인접 칸으로 퍼져나갈 수 있음
# 바이러스의 확산을 막기 위해 벽을 세워야 함(3개 꼭 맞춰서)
# 0: 빈 칸, 1: 벽, 2: 바이러스
# 벽을 세우지 않는다면? 바이러스는 모든 빈 칸으로 퍼져나갈 수 있음
# 벽을 3개 세우고, 바이러스를 쭉 퍼뜨려보자. 그 후 바이러스가 퍼지지 않은 부분의 넓이를 x라고 하자.
# 그 x의 최댓값을 구하여 보자.

N, M = map(int, input().split()) # N: 세로 크기, M: 가로 크기
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_arr = []
# 완전탐색
# 조합으로 빈 칸중 3개의 칸을 골라내보자
# 각 케이스마다 바이러스가 모두 퍼진 후의 모습을 그려보고, 그때의 0의 개수를 cnt에 저장하며 세어보자
# 초기 ans 값을 0으로 두고, cnt값이 기존의 ans보다 클 경우 ans에 cnt 값을 할당해주자

# 로직
# 1. 0이 들어있는 좌표를 쭉 받아온다
# 2. 좌표들중 3개의 값을 골라 그 값에 해당하는 위치를 0에서 1로 바꾼다
# 3. 바이러스를 퍼뜨린다
# 4. 0의 개수를 센다
# 5. ans값과 비교하여 더 클 경우 갱신한다

make_cho()
comb = list(combinations(cnt_arr, 3)) # 이 조합을 쭉 돌면서 값을 1로 바꿔준 후 바이러스의 퍼트림 결과를 정리해보자.
ans = 0

# 조합별로 실험해보자
for i in comb:
    test_arr = deepcopy(arr)  # arr의 값을 받아 바이러스를 퍼뜨려 볼 리스트
    test_arr[i[0][0]][i[0][1]] = 1
    test_arr[i[1][0]][i[1][1]] = 1
    test_arr[i[2][0]][i[2][1]] = 1
    imshi = find_cnt()
    del(test_arr)
    if ans < imshi:
        ans = imshi

print(ans)