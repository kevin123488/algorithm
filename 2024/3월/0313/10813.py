import sys
sys.stdin = open('10813.txt')

n, m = map(int, input().split())
change_method = [list(map(int, input().split())) for _ in range(m)]

# 바구니 n개, 1 ~ n까지의 번호가 메겨져 있음, m번 교환

basket = []
for i in range(n + 1):
    basket.append(i)

for i in change_method:
    change_1 = i[0]
    change_2 = i[1]
    basket[change_1], basket[change_2] = basket[change_2], basket[change_1]

for i in range(1, len(basket)):
    print(basket[i], end=' ')