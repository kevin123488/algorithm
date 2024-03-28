import sys
sys.stdin = open('input1107.txt')
from collections import deque
input = sys.stdin.readline

def make_num(length):
    q = deque()
    num = ''
    q.append(num)
    ans_list = []
    while True:
        now = q.popleft()
        if len(now) == length + 1:
            break
        if len(now) == length:
            ans_list.append(int(now))
        for i in range(10):
            if i not in non_fixed:
                q.append(now + str(i))

    return_ans = 10**10
    for i in ans_list:
        return_ans = min(return_ans, i-n)

    return return_ans

n = int(input())
m = int(input())
non_fixed = []
if m != 0:
    non_fixed = list(map(int, input().split()))
else:
    print(make_num(len(str(n))))