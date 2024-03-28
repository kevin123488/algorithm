import sys
sys.stdin = open('input2493.txt')
input = sys.stdin.readline

def find_ans(i):
    # print(arr[0:i]) # 조회 대상인 값의 위치 이하인 부분을 대상으로 조회
    # 9일때 6, 5일때 9, 6 순으로 조회하도록 짜자
    for j in range(len(arr[0:i])-1, -1, -1):
        if arr[0:i][j] >= arr[i]:
            ans[i] = j + 1
            break

# 일직선 위에 N개의 높이가 서로 다른 탑을 왼쪽에서 오른쪽 방향으로 세우자
# 각 탑의 꼭대기에 레이저 송신기 설치
# 모든 탑의 레이저 송신기는 레이저 신호를 수평 직선의 왼쪽 방향으로 발사
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
# 6 9 5 7 4 탑이 이렇게 놓여 있으면
# 4가 쏜 레이저는 7이, 7이 쏜 레이저는 9가, 5가 쏜 레이저도 9가, 9와 6이 쏜 레이저는 아무도
# 수신하지 못하게 된다.
# 탑의 수와 그 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지 알아내는
# 프로그램 작성

N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N
for i in range(1, N):
    find_ans(i)

for i in ans:
    print(i, end=" ")