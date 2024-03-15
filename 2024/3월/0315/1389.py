import sys
sys.stdin = open('1389.txt')
from collections import deque

def bfs(person, find_person, visited):
    q = deque()
    visited[person] = 1
    q.append([person, 0]) # 현재 만나고있는 사람과 그 사람을 만나는데 거쳤던 단계

    while q:
        np, na = q.popleft()
        if np == find_person:
            return na
        
        for i in friend_list[np]: # 지금 만나고있는 사람을 통해 만날 수 있는 사람
            if visited[i] == 0:
                q.append([i, na + 1])
                visited[i] = 1


def find_friend(person, n):
    ans = 0
    for i in range(1, n + 1):
        if i != person:
            visited = [0] * (n + 1)
            ans += bfs(person, i, visited)

    return ans


n, m = map(int, input().split())

friend_list = [[] for _ in range(n + 1)] # i번 인덱스에 i번의 친구가 들어가있음

for i in range(m):
    friend_1, friend_2 = map(int, input().split())
    friend_list[friend_1].append(friend_2)
    friend_list[friend_2].append(friend_1)


# 모든 인원에 대해 다른 친구에게 도달하는데 필요한 단계의 수의 합을 계산해보자
# 1에 대해 2, 3, 4, 5까지 도달하는데 필요한 단계의 합
# 2에 대해 1, 3, 4, 5까지 도달하는데 필요한 단계의 합
# ...
# 5에 대해 1, 2, 3, 4까지 도달하는데 필요한 단계의 합
# 구한 단계의 합들 중 가장 적은 값을 갖는 케이스의 인원의 번호를 출력
# 여러명일 경우 번호가 적은 사람 출력

ans = 100000
min_friend = 0
for i in range(1, n + 1):
    now_ans = find_friend(i, n)
    if now_ans < ans:
        min_friend = i
        ans = now_ans

print(min_friend)