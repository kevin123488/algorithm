import sys
sys.stdin = open('input14500.txt')
from collections import deque
import time

# 델타탐색
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# ㅗ 모양 탐색
def make_o(i, j, ans):
    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if k == 0:
                ans1 = arr[ni][nj]
            elif k == 1:
                ans2 = arr[ni][nj]
            elif k == 2:
                ans3 = arr[ni][nj]
            else:
                ans4 = arr[ni][nj]

    return_1 = ans1 + ans2 + ans3 + arr[i][j]
    return_2 = ans1 + ans3 + ans4 + arr[i][j]
    return_3 = ans1 + ans2 + ans4 + arr[i][j]
    return_4 = ans2 + ans3 + ans4 + arr[i][j]

    return max(ans, return_1, return_2, return_3, return_4)

# 4칸 탐색하는 함수 완탐돌리기
# 이 문제는 bfs로 풀 수 없다. 완탐 케이스ㅢ 방문기록 처리가 곤란하기 때문
# dfs 로 완전탐색을 해준 후
# def bfs(i, j, ans):
#     q = deque()
#     temp = 0
#     cnt = 0
#     visited[i][j] = 1
#     q.append([[i, j], temp, cnt, visited])
#     while q:
#         start = q.popleft()
#         if start[2] == 4:
#             if start[1] > ans:
#                 ans = start[1]
#         for k in range(4):
#             ni = start[0][0] + di[k]
#             nj = start[0][1] + dj[k]
#             if 0 <= ni < N and 0 <= nj < M and start[3][ni][nj] == 0:
#                 start[3][ni][nj] = 1
#                 q.append([[ni, nj], start[1] + arr[ni][nj], start[2] + 1, start[3]])
#
#     return ans

def dfs(i, j, cnt, find):
    global ans
    if find + (max_only) * (4-cnt) <= ans:
        return
    if cnt == 4:
        ans = max(ans, find)
        return ans
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, cnt + 1, find + arr[ni][nj])
            visited[ni][nj] = 0


start = time.time()
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오 (회전 혹은 대칭 가능)
ans = 0
max_only = max(map(max, arr))
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, 0)
        ans = make_o(i, j, ans)
        print(visited)
        visited[i][j] = 0
end = time.time()
print(ans)
print(end - start)