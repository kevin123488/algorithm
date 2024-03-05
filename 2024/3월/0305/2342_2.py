n, m = map(int, input().split())

basket = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split()) # i번 바구니부터 j번 바구니까지 k번 공을 넣는다는 의미
    for x in range(i, j + 1):
        if len(basket[x]) == 0:
            basket[x].append(k)
        else:
            basket[x] = [k]

for i in range(1, len(basket)):
    if len(basket[i]) == 0:
        print(0, end=' ')
    else:
        print(basket[i][0], end=' ')