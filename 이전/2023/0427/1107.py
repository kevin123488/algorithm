import sys
from collections import deque
sys.stdin = open('input1107.txt')
input = sys.stdin.readline

def find_ans(ans):
    now = 100
    q = deque()
    num_clicked = False
    q.append([now, ans, num_clicked])
    while q:
        now_ch, now_ans, now_num_clicked = q.popleft()
        if now_ch == n:
            return now_ans
        for i in use_remote:
            if i == '+':
                q.append([now_ch + 1, now_ans + 1, False])
            elif i == '-':
                if now == 0:
                    pass
                else:
                    q.append([now_ch - 1, now_ans + 1, False])
            else:
                if now_num_clicked == True:
                    q.append([int(str(now_ch)+str(i)), now_ans + 1, True])
                else:
                    q.append([i, now_ans + 1, True])



n = int(input()) # 목표 채널
m = int(input()) # 고장난 버튼 수

# tv를 보던 수빈이. 리모컨을 박살내고 마는데
# 리모컨에는 0~9와 +, - 버튼이 있다. 0에서 -버튼 누르면 채널은 변하지 않는다.
# 수빈이가 이동하려고 하는 채널은 n이다. 고장난 버튼이 주어졌을 때, 채널 n으로 이동하기 위해 최소 몇 번
# 버튼을 눌러야 하는지 구하라
# 현재 채널은 100번이다

# 사용 가능한 버튼을 모아두자
non_fixed = []
remote = ['+', '-', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
use_remote = []
if m != 0:
    non_fixed = list(map(int, input().split()))
for i in remote:
    if i not in non_fixed:
        use_remote.append(i)

ans = 0
print(find_ans(ans))