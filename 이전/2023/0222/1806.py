import sys
sys.stdin = open('1806input.txt')

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# 연속된 수들의 부분합 중 그 합이 S 이상이 되는 것 중 가장 짧은 것의 길이를 구해보자
# S 이상이 되는 합을 만들 수 없다면 0을 출력하자
# 투 포인터 사용하자

noo_jeuk = 0
noo_jeuk_list = [0]
for i in arr:
    noo_jeuk += i
    noo_jeuk_list.append(noo_jeuk)

# arr = [1, 2, 3, 4, 5]
# noo_jeuk_list의 특정 인덱스에 해당하는 값은 arr의 인덱스 0부터 해당 인덱스까지의 합
# noo_jeuk_list = [1, 3, 6, 10, 15]
# noo_jeuk_list[i] - noo_jeuk_list[j]

ans = N + 1
len = 1
start = 1
while start <= N:
    if noo_jeuk_list[start] >= S:
        if noo_jeuk_list[start] - noo_jeuk_list[start - len] < S:
            len += 1
            if len > start:
                start += 1
        else:
            if ans > len:
                ans = len
            len = 1
            start += 1
    else:
        start += 1

if ans == N + 1:
    print(0)
else:
    print(ans)