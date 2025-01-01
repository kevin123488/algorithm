import sys
sys.stdin = open('2166.txt')

n = int(input())
x_y_list = [list(map(int, input().split())) for _ in range(n)]
# print(n, x_y_list)

x_y_list += [x_y_list[0]]
# print(x_y_list)

ans = 0
for i in range(n):
    ans += x_y_list[i][0] * x_y_list[i + 1][1]
    ans -= x_y_list[i][1] * x_y_list[i + 1][0]

print(round(abs(ans) * 0.5, 1))