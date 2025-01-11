import sys
sys.stdin = open('input_2533.txt')
sys.setrecursionlimit(1000000)

def dfs(start):
    visited[start] = 1

    if len(friendship[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    
    else:
        for i in friendship[start]:
            if visited[i] == 1:
                continue
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])
        dp[start][1] += 1

n = int(sys.stdin.readline())
friendship = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    friendship[a].append(b)
    friendship[b].append(a)

# 자신의 모든 친구가 얼리어답터 일 때 새로운 아이디어를 받아들임
# 아이디어를 전파하는데 필요한 얼리어답터의 최소 명수를 출력하는 프로그램을 작성하자

dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)

dfs(1)

print(min(dp[1][0], dp[1][1]))