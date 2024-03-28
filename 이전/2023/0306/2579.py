import sys
sys.stdin = open('2579input.txt')
from collections import deque

def bfs():
    q.append([0, 0, 0]) # 현재 위치(시작점은 0)와 가중치의 함, 그리고 연속 몇 칸을 거쳤는지 저장
    ans = 0
    while q:
        start = q.popleft()
        if start[0] == s:
            if ans < start[1]:
                ans = start[1]
        if start[0] + 1 <= s and start[2] < 2:
            q.append([start[0] + 1, start[1] + s_score[start[0] + 1], start[2] + 1])
        if start[0] + 2 <= s:
            q.append([start[0] + 2, start[1] + s_score[start[0] + 2], 1])

    return ans

s = int(input())
s_score = [0]
for i in range(s):
    s_score.append(int(input()))

# 계단을 밟으면 해당 계단에 쓰여 있는 점수를 얻게 됨
# 계단 오르는 규칙
# 한번에 한개 혹은 두개 오를 수 있음
# 연속된 세 개의 계단을 모두 밟아선 안됨. 시작점은 계단에 포함되지 않음
# 마지막 도착 계단은 반드시 밟아야 함
# 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구해보자
q = deque()
print(bfs())