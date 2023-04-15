import sys
sys.stdin = open('input1010.txt')
input = sys.stdin.readline

# 서쪽 n개 사이트, 동쪽 m개 사이트. n <= m
# 서쪽 사이트와 동쪽 사이트를 다리로 연결하려 함
# 한 사이트에는 최대 한개의 다리만 연결 가능
# n개만큼의 다리를 지으려 한다. 서로 겹쳐질 수 없다고 할 때, 다리를 지을 수 있는 경우의 수를 구하라
# 서쪽 사이트 1번과 2번을 예로 들어보자. 1번과 연결된 동쪽 사이트는 2번과 연결된 동쪽 사이트보다 번호가 낮아야 한다.

t = int(input())
for tc in range(t):
    n, m = map(int, input().split()) # 4 7
    # mCn = 7654/4321
    ans = 1
    for i in range(m, m-n, -1): # 7, -1, 3 -> 7, 6, 5, 4
        ans *= i

    for i in range(1, n+1):
        ans //= i

    print(ans)