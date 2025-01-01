import sys
sys.stdin = open('12852.txt')

def min_operations_to_one(n):
    dp = [0] * (n + 1)  # DP 테이블 초기화
    sequence = [[] for _ in range(n + 1)]  # 각 숫자에 대한 연산 수행 경로 저장
    
    for i in range(2, n + 1):
        # 1을 빼는 연산으로 초기화
        dp[i] = dp[i - 1] + 1
        sequence[i] = sequence[i - 1] + [i - 1]  # 이전 숫자에서 1을 뺀 수를 경로에 추가
        
        # 2로 나누어 떨어지는 경우
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            sequence[i] = sequence[i // 2] + [i // 2]  # 이전 숫자에서 2로 나눈 수를 경로에 추가
        
        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            sequence[i] = sequence[i // 3] + [i // 3]  # 이전 숫자에서 3으로 나눈 수를 경로에 추가
    
    return dp[n], sequence[n]

# 예시
n = int(input())
min_ops, path = min_operations_to_one(n)
print(min_ops)
ans_list = [n] + path[::-1]
for i in ans_list:
    print(i, end=' ')