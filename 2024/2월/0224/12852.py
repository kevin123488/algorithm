import sys
sys.stdin = open('12852.txt')
from collections import deque

def bfs(n):
    q = deque()
    q.append([n, [n]]) # [2, [2]]

    while q:
        now, ans_list = q.popleft() # [1, [2, 1]]
        if now == 1:
            print(len(ans_list) - 1)
            for i in ans_list:
                print(i, end=' ')
            break

        if now % 3 == 0:
            ans_list_temp = ans_list + [now // 3]
            q.append([now // 3, ans_list_temp])

        if now % 2 == 0:
            ans_list_temp = ans_list + [now // 2]
            q.append([now // 2, ans_list_temp]) # [[1, [2, 1]]]

        ans_list_temp = ans_list + [now - 1]
        q.append([now - 1, ans_list_temp]) # [[1, [2, 1]], [1, [2, 1]]]

    return

# 연산 종류  3가지. 3으로 나누어 떨어지면 3으로 나눔, 2로 나누어 떨어지면 2로 나눔, 1을 뺌
# 정수 N에 대해 위의 3가지 연산을 활용하여 1을 만들고자 함. 연산을 사용하는 횟수 최솟값을 출력

n = int(input())

# 첫 줄에 연산 횟수 최솟값출력
# 둘째줄에 n을 1로 만드는 과정을 수의 순서대로 출력

bfs(n)