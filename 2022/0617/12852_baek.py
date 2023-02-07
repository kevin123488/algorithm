import sys
sys.stdin = open('12852_input.txt')

def dev_3(N):
    return N//3

def dev_2(N):
    return N//2

def minus(N):
    return N-1

def dfs(N, cnt):
    global max_cnt
    ans_list.append(N)
    if N == 1:
        max_cnt = cnt
        return max_cnt
    if cnt >= max_cnt:
        return

    for i in range(3):
        if i == 0 and N % 3 == 0:
            cnt += 1
            dfs(dev_3(N), cnt)
            cnt -= 1
        if i == 1 and N % 2 == 0:
            cnt += 1
            dfs(dev_2(N), cnt)
            cnt -= 1
        if i == 2:
            cnt += 1
            dfs(minus(N), cnt)
            cnt -= 1



N = int(input())

cnt = 0
max_cnt = 10000000000000
ans_list = []
dfs(N, cnt)
print(max_cnt)
print(ans_list)