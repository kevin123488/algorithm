import sys
sys.stdin = open('9252.txt')

a = input()
b = input()

lcs = ''
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, 1 + len(a)):
    for j in range(1, 1 + len(b)):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(a)][len(b)])

len_a = len(a)
len_b = len(b)

while len_a > 0 and len_b > 0:
    if a[len_a - 1] == b[len_b - 1]:
        lcs += a[len_a - 1]
        len_a -= 1
        len_b -= 1
    elif dp[len_a - 1][len_b] > dp[len_a][len_b - 1]: # 문자열 a의 마지막 단어 제외한 부분까지와 b의 공통부분이 
        len_a -= 1
    else:
        len_b -= 1

ans = ''
for i in range(len(lcs) - 1, -1, -1):
    ans += lcs[i]

print(ans)