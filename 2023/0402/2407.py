import sys
sys.stdin = open('input2407.txt')

n, m = map(int, input().split())
# 10C4 -> 10 * 9 * 8 * 7 / (1 * 2 * 3 * 4)
ans = 1
for i in range(n, n - m, -1):
    ans *= i

di = 1
for i in range(1, m + 1):
    di *= i

print(ans // di)