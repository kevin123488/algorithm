import sys
from itertools import combinations, permutations
sys.stdin = open('input15650.txt')
input = sys.stdin.readline

def dfs(cnt, temp):
    if cnt == M:
        for i in temp:
            print(i, end=" ")
        print()
        return
    for i in range(len(arr)):
        if temp == []:
            temp.append(arr[i])
            dfs(cnt + 1, temp)
            temp.pop(-1)
        elif temp[-1] > arr[i]:
            pass
        else:
            temp.append(arr[i])
            dfs(cnt + 1, temp)
            temp.pop(-1)

N, M = map(int, input().split())
# arr = list(combinations(list(i for i in range(1, 1 + N)), M))
# for i in arr:
#     for j in range(len(i)):
#         print(i[j], end=" ")
#     print()
arr = list(i for i in range(1, N + 1))
cnt = 0
temp = []
dfs(cnt, temp)