import sys
sys.stdin = open('input11404.txt')
input = sys.stdin.readline

# n개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다.
# 각 버스는 한 번 사용할 때 필요한 비용이 있다.
# 모든 도시의 쌍(A, B)에 대해 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하자.

def war_f(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                near[j][k] = min(near[j][k], near[j][i] + near[i][k])
                if j == k:
                    near[j][k] = 0

n = int(input())
m = int(input())
# arr = [list(map(int, input().split())) for _ in range(m)] # (버스 시작 도시, 버스 도착 도시, 한 번 타는데 필요한 비용)
# 인접행렬로 구현
near = [[100000000] * (n+1) for _ in range(n+1)]
for i in range(m):
    start, end, value = map(int, input().split())
    near[start][end] = min(near[start][end], value)

war_f(n)

for i in range(1, len(near)):
    for j in near[i][1:]:
        if j == 100000000:
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()