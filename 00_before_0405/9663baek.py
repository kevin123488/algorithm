# N-Queen 문제는 크기가 N*N인 체스판 위에 퀸 N개를 서로
# 공격할 수 없게 놓는 문제이다
# N이 주어졌을 때 퀸을 놓는 방법의 수를 구하여라

# 2*2 배열이라고 가정하면
# 인덱스에 0 넣기, 포문, 첫째줄에 체스 놓기, 인덱스에 1 넣기, 포문, 둘째줄에 체스 놓기, 인덱스에 2 넣기
# def dfs(idx):
#     global ans
#     if idx == N:
#         ans += 1
#         return

#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(idx+1)
#             visited[i] = 0

# N = int(input())
# ans = 0
# visited = [0]*N # 방문표시
# dfs(0) # 0부터 조회 시작
# print(ans)

def dfs(idx):
    global ans
    if idx == N:
        ans += 1
        return
    for i in range(N):
        visited[idx] = i
        if ad(idx):
            dfs(idx+1)

def ad(idx):
    for i in range(idx):
        if visited[idx] == visited[i] or abs(visited[idx] - visited[i]) == idx - i:
            return False
    return True

N = int(input())
visited = [0]*N
ans = 0
dfs(0)
print(ans)