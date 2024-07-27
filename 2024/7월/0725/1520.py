import sys
sys.stdin = open('1520.txt')

# 경로에서 낮은 블럭으로만 이동 가능
# 상하좌우로만 이동 가능
# 0, 0 에서 m - 1, n - 1까지 이동하는 경로의 수 출력
# 이거 DP로 가야하는데 솔직히 (일반적으로 볼 때)쉽지는 않은듯
# 하지만 나에겐 쉬움

m, n = map(int, input().split())
road_map = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(m)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

