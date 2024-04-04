# 일정 피로도를 이용해 던전을 탐색할 수 있음
# 던전에 진입하기 위해 최소로 지녀야하는 피로도가 있고, 던전을 클리어한 후 소모해야하는 피로도가 있음
# 유저의 피로도가 주어질 때, 던전을 최대로 탐색하는 경우 몇 개의 던전을 탐색할 수 있는지 return (던전당 1회만 가능)

def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeons)):
        if visited[i] == 0 and dungeons[i][0] <= k:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = 0
    
    return answer

def solution(k, dungeons):
    global answer
    answer = -1

    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons, visited) # 0 자리는 방문한 던전의 수
    return answer


k = 80
dungeons = [[80,20],[50,40],[30,10]] # [진입하기 위해 필요한 피로도, 탐색 후 소모되는 피로도]

print(solution(k, dungeons))