import sys
sys.stdin = open('15685input.txt')
sys.setrecursionlimit(100000)

N = int(input()) # 드래곤커브 갯수
dragoncurves = []
for i in range(N): # N개의 줄에 드래곤커브의 정보가 주어짐
    dragoncurves.append(list(map(int, input().split())))
    # x, y, d, g로 구성

# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)
# 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
# 방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.
# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)

