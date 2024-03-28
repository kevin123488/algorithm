import sys
from collections import deque
sys.stdin = open('1916input.txt')

def find_least(start):
    idx = False
    min = 10**9
    for i in range(len(arr[start])):
        if visited[arr[start][i][0]] == 0 and min > arr[start][i][1]:
            idx = arr[start][i][0]
            min = arr[start][i][1]
    return idx

def di(start):
    k = find_least(start)
    q.append(k)
    while q:
        finding = q.popleft()
        visited[finding] = 1
        for i in arr[finding]:
            if ans_list[i[0]] > ans_list[finding] + i[1]:
                ans_list[i[0]] = ans_list[finding] + i[1]
                q.append(i[0])
        k = find_least(start)
        if k:
            q.append(k)

N = int(input())
M = int(input())
arr = [[] for i in range(N+1)]
for i in range(M):
    k, l, m = map(int, input().split())
    arr[k].append([l, m]) # arr의 인덱스가 출발점, 추가되는 리스트의 첫 값이 시작점, 두번째 값이 가중치

start, end = map(int, input().split())
visited = [0] * (N+1)
ans_list = [10**9] * (N+1)
for i in arr[start]:
    if ans_list[i[0]] > i[1]:
        ans_list[i[0]] = i[1]

q = deque()
di(start)
print(ans_list[end])