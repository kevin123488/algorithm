import sys
sys.stdin = open('input1003.txt')
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    dp_0 = [0] * (n + 1) # 인덱스 0부터 n까지
    dp_1 = [0] * (n + 1)
    if n == 0:
        print(1, 0)
    else:
        dp_1[1] = 1
        for i in range(2, n + 1): # i 범위 2부터 n까지
            dp_0[i] = dp_1[i - 1]
            dp_1[i] = dp_0[i - 1] + dp_1[i - 1]

        print(dp_0[n], dp_1[n])
    # cnt0, cnt1
    # 1 -> 0, 1
    # 2 -> 1, 1
    # 3 -> 1, 2
    # 4 -> 2, 3
    # 5 -> 3, 5
    # 6 -> 5, 8
    # 7 -> 8, 13
    # 8 -> 13, 21
    # dp_0[n] = dp_1[n-1]
    # dp_1[n] = dp_0[n-1] + dp_1[n-1]