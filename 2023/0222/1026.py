import sys
sys.stdin = open('1026input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 큰 수에 작은 수를 곱하면 된다.
# 즉 B의 최댓값과 A의 최솟값을 매칭시키면 된다는 얘기
A.sort()
B.sort()
B.reverse()

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)