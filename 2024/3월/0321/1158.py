import sys
sys.stdin = open('1158.txt')

def find_idx(idx, n):
    while True:
        if idx >= n:
            idx -= n
        else:
            break
    
    return idx

n, k = map(int, input().split())

# 1 ~ n까지 n명의 사람이 원을 이루며 앉아있음
# 양의 정수 K
# 순서대로 K번째 사람 제거
# 한 사람 제거 -> 남은 사람들로 이루어진 원을 따라 이 과정을 계속
# N명의 사람이 제거될 때 까지 계속됨

# 원형큐 구현
round_q = []
for i in range(1, n + 1):
    round_q.append(i)

idx = -1 # 삭제할 인덱스
ans_q = []

while True:
    idx += k
    idx = find_idx(idx, n)

    ans_q.append(round_q.pop(idx))
    n -= 1
    idx -= 1

    if n == 0:
        break

print('<', end='')
for i in range(len(ans_q)):
    print(ans_q[i], end='')
    if i == len(ans_q) - 1:
        pass
    else:
        print(',', end=' ')

print('>')