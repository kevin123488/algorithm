import sys
sys.stdin = open('2805_input.txt')

N, M = map(int, sys.stdin.readline().split())
# N, M = map(int, input().split())
# 나무 M미터가 필요
# 높이 H 지정. 그러면 톱날이 땅으로부터 H미터 위로 올라감. (H는 0과 양의 정수 중 하나)
# 집 근처 나무 한 줄에 대한 벌목을 허가받음
# 15 20 25 5 나무의 높이가 다음과 같다고 하자. H가 15라고 한다면
# 잘린 후의 나무들의 높이는 15, 15, 15, 5(얘는 H보다 높이가 낮기 때문에 잘리지 않았음)가 될 것.
# 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정 가능한 높이의 최댓값을 구하자

arr = list(map(int, sys.stdin.readline().split()))
# arr = list(map(int, input().split()))
# print(arr)
# 각 나무들에서 H값을 뺀 값(A)들을 더해서 M이상인 되어야 함. (A가 0이하일 경우 해당 A는 0 처리)
# 어떤 값을 설정. 해당 값을 설정했을 때 나오는 총 합이 M보다 클 경우, 어떤 값보다 큰 값을 범위로 하여 다시 총 합 계산
# 총 합이 M보다 작을 경우, 어떤 값보다 작은 값을 범위로 하여 다시 총 합 계산

