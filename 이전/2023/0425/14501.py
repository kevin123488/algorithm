import sys
sys.stdin = open('input14501.txt')
input = sys.stdin.readline

n = int(input())
t = []  # 상담을 완료하는데 걸리는 기간 리스트
p = []  # 상담을 완료했을 때 받을 수 있는 금액 리스트
dp = [0] * (n+1)  # dp[i]: i일까지 얻을 수 있는 최대 수익

# 입력 받기
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

# DP 알고리즘 수행
for i in range(n-1, -1, -1): # 6~0까지 순회
    if i + t[i] > n:  # 상담 기간이 퇴사 전에 끝나지 않는 경우
        dp[i] = dp[i+1]
    else:  # 상담 기간이 퇴사 전에 끝나는 경우
        # i가 3일 때
        dp[i] = max(dp[i+1], dp[i+t[i]]+p[i])
    # print(dp)

print(dp[0])