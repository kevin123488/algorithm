import sys
sys.stdin = open('11659input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
noo_jeuk_list = [0]
temp = 0
for i in arr:
    temp += i
    noo_jeuk_list.append(temp)

for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(noo_jeuk_list[j] - noo_jeuk_list[i-1])