import sys
sys.stdin = open('input_13023.txt')

def dfs(friend_list, cnt, visited, now_person):
    global answer
    # now_person의 친구 목록: friend_list[now_person]
    # now_person 기준 이전 사람과 다음 사람이 동일하면 안됨. 그 외에는 가능
    visited[now_person] = 1
    if cnt == 4:
        answer = 1
        return
    
    for i in friend_list[now_person]:
        if visited[i] == 0:
            dfs(friend_list, cnt + 1, visited, i)
    
    visited[now_person] = 0


n, m = map(int, input().split())
# 0 ~ n-1의 사람이 있음
# 친구관계 입력
friend_list = [[] for _ in range(n)] # n명의 사람, friend_list[0] => 0이라는 사람의 친구 목록
for i in range(m):
    friend_1, friend_2 = map(int, input().split())
    friend_list[friend_1].append(friend_2)
    friend_list[friend_2].append(friend_1)

# 친구관계중 a-b, b-c, c-d, d-e 형식의 친구 구조가 존재하는지 아닌지를 판별하는 것이 문제
# -> 친구 파도타기를 할 때 친구 판별이 4회 이상 연속해서 이루어지면 됨

visited = [0] * n
answer = 0
for i in range(n):
    dfs(friend_list, 0, visited, i)
    if answer == True:
        break

print(answer)