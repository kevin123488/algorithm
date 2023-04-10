import sys
from collections import deque
sys.stdin = open('input1149.txt')
input = sys.stdin.readline

def bfs(ans):
    q = deque()
    for i in range(3):
        q.append([i, 0, arr[0][i]]) # 색과 몇 번째 집인지, 그리고 그 때의 가중치의 합을 저장

    while q:
        now = q.popleft()
        before_color = now[0]
        house_level = now[1]
        before_ans = now[2]
        if house_level == n-1:
            ans = min(ans, before_ans)
            continue
        for i in range(3):
            if i != before_color:
                q.append([i, house_level + 1, before_ans + arr[house_level + 1][i]])

    return ans


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# rgb 거리에는 집이 n개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 n번 집이 순서대로 있다.
# 집은 빨, 초, 파중 하나의 색으로 칠해야 함
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자
# 1번 집의 색은 2번 집의 색과 같지 않아야 함
# n번 집의 색은 n-1번 집의 색과 같지 않아야 함
# i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 간단히 말해 연속된 두 집의 색이 같으면 안됨
ans = 10000000
print(bfs(ans))