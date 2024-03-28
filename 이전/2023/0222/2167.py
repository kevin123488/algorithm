import sys
sys.stdin = open('2167input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
option_list = []
for i in range(K):
    option_list.append(list(map(int, input().split())))

for a in option_list:
    i, j, x, y = a[0]-1, a[1]-1, a[2]-1, a[3]-1 # 인덱스 값으로 보정
    ans = 0
    for z in range(N):
        for w in range(M):
            if i <= z <= x and j <= w <= y:
                ans += arr[z][w]
    print(ans)