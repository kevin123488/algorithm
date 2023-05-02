import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('input15683.txt')
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 0, 0]) # cctv i, cctv j, 방향, cctv 종류
    while True:
        for i in range(n):
            for j in range(m):
                if 0 < office[i][j] < 6:
                    for k in range(4):
                        q.append([i, j, k, office[i][j]])

n, m = map(int, input().split()) # n은 세로, m은 가로
office = [list(map(int, input().split())) for _ in range(n)]

# 로직
# 모든 cctv에 대해서 90도씩 돌려간 결과를 이용, 완전탐색하자
# 리스트에 각 cctv의 방향을 0, 1, 2, 3 값중 하나로 저장해두자
# ex) case1: [0, 0, 1, 1, 0, 2, 1, 3], cctv의 순서는 순차적으로 순회했을 때의 순서
# 위와 같은 cctv의 방향 정보 저장 리스트를 모든 경우에 대해 제작하고, 해당 리스트에 해당하는 사각지대의 수를 찾아내자
# 그 값중 최솟값을 출력

bfs()