import sys
sys.stdin = open('input14720.txt')
input = sys.stdin.readline

n = int(input())
milk = list(map(int, input().split()))
# 딸 -> 초 -> 바 -> 딸
# 0: 딸, 1: 초, 2: 바
ans = 0
before_milk = ''
for i in range(n):
    if before_milk == '':
        if milk[i] == 0:
            ans += 1
            before_milk = 0
    else:
        if before_milk == 0 and milk[i] == 1:
            ans += 1
            before_milk = 1
        elif before_milk == 1 and milk[i] == 2:
            ans += 1
            before_milk = 2
        elif before_milk == 2 and milk[i] == 0:
            ans += 1
            before_milk = 0

print(ans)