import sys
sys.stdin = open('input15666.txt')
input = sys.stdin.readline

def dfs(cnt, temp):
    if cnt == M:
        ans = tuple(sorted(temp))
        if ans not in ans_list:
            print(*ans)
            ans_list.append(ans)
        return
    for i in range(len(arr)):
        temp.append(arr[i])
        dfs(cnt + 1, temp)
        temp.pop(-1)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
temp = []
ans_list = []
dfs(cnt, temp)
ans_list = list(ans_list)
ans_list.sort()
# for i in ans_list:
#     for j in i:
#         print(j, end=" ")
#     print()
