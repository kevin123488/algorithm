import sys
sys.stdin = open('input1024.txt')
input = sys.stdin.readline

n, l = map(int, input().split())
# 합이 n, 길이가 적어도 l인 가장 짧은 연속된 정수 리스트(음이 아니어야 함. 0은 가능)
# 없으면 -1 출력
# n을 l로 나눈 값이 존재한다 -> l개의 리스트는 만들 수 없다.
# n을 l + a로 나눈 값이 정수가 아니게 될 때, 그 개수만큼의 리스트를 만들 수 있다.
# n을 a로 나눈 값이 정수로 나뉘어 떨어지면서 a가 홀수이다 -> 나뉘어 떨어지는 값 전후로 계싼
# n을 a로 나눈 값이 정수로 나뉘어 떨어지면서 a가 짝수이다 -> 안됨
# n을 a로 나눈 값이 .5로 나오면서 a가 짝수이다 -> .5 앞의 값과 뒤의 값 전후로 계싼
# 그 외 -> 찾을 수 업음

mid_ans = 0
len_list = 0

for i in range(n-l+1):
    a = l + i
    if a%2:
        if n//a == n/a:
            mid_ans = n//a
            len_list = a
            break
    else:
        if str(n/a)[-1] == '5' and str(n/a)[-2] == '.':
            mid_ans = n/a
            len_list = a
            break

if len_list > 100:
    print(-1)
else:
    if len_list%2:
        # mid_ans값 전으로 len_list//2개 만큼 간 값에서 len_list개 만큼 출력
        start = mid_ans - len_list//2
        for i in range(start, start + len_list):
            if i < 0:
                print(-1)
                break
            print(i, end=' ')
    else:
        # mid_ans값 전으로 len_list//2개 만큼 간 값에서 len_list개 만큼 출력
        start = int(mid_ans) - len_list//2 + 1
        for i in range(start, start + len_list):
            if i < 0:
                print(-1)
                break
            print(i, end=' ')