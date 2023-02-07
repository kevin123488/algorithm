import sys
sys.stdin = open('2775.txt')

# 아파트 거주 조건
# a층의 b호에 살기 위해선 자신의 아래층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 함
# 아파트에 빈 집 없음, 모든 거주민들이 이 조건을 지키고 있음

# 주어지는 양의 정수 k와 n에 대해 k층의 n호에는 몇 명이 살고 있는지 출력하시오
# 아파트는 0층부터 있음, 각 층은 1호부터 있음, 0층 i호에는 i명이 살고있음

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    # 0층부터 쭉 채워가는게 좋지 않을까?
    # k층 n호면 일단 (k+1)*n의 이차원 리스트를 만들 필요가 있어보인다
    # k층 -> 세로열, n호 -> 가로행
    arr = [[0]*n for _ in range(k+1)]

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j] = j+1 # 호수는 1호부터 시작하기 때문
            else:
                arr[i][j] = sum(arr[i-1][:j]) + arr[i-1][j]

    print(arr[k][n-1])