import sys
sys.stdin = open('11724input.txt')
sys.setrecursionlimit(100000)

def dfs(n):
    visited[n] = 1
    # 돌면서 방문한 곳은 1 표시
    for i in range(len(arr[n])): # arr의 n번째 요소를 쭉 훑으면서
        if arr[n][i] == 1 and visited[i] == 0: # 연결되어 있으면서 아직 방문하지 않은 곳일 경우
            visited[i] = 1 # 방문표시 해주고
            dfs(i)
    return

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
N, M = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수
ganseun_list = []
arr_size = 0
for i in range(M):
    u, v = map(int, input().split())
    ganseun_list.append([u, v])

# 덩어리가 몇 개 나오는지 확인하면 되는 문제
# 2차원 리스트를 하나 만들자
arr = [[0] * (N + 1) for _ in range(N + 1)] # 인덱스와 값을 일치시키기 위함
visited = [0] * (N + 1)
for i in ganseun_list:
    arr[i[0]][i[1]] = 1 # 간선의 연결 정보를 1로 표현
    arr[i[1]][i[0]] = 1
# 그래프의 연결 관계를 이차원 리스트에 표현했음
#     0, 1, 2, 3, 4, 5, 6
# 0 [[0, 0, 0, 0, 0, 0, 0],
# 1  [0, 0, 1, 0, 0, 1, 0],
# 2  [0, 1, 0, 0, 0, 1, 0],
# 3  [0, 0, 0, 0, 1, 0, 0],
# 4  [0, 0, 0, 1, 0, 0, 1],
# 5  [0, 1, 1, 0, 0, 0, 0],
# 6  [0, 0, 0, 0, 1, 0, 0]]

# dfs 사용하면 될 것 같음
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
    if visited == [0] + [1] * N:
        break

# 5 1
# 2 3
# 2가 나오는 이유?
#

print(cnt)