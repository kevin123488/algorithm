import sys
sys.stdin = open('15311.txt')

n = int(input())

# 2000개의 나열된 수 중 어떤 연속된 부분을 더하면 1 ~ 100만까지의 모든 수를 표현 가능하다
# 각 수는 1 ~ 100만
# 가운데를 기준으로 1 ~ 999까지는 앞의 1로 만들고, 그 이후부터는 1000으로 하면 됨

ans_list = []
for i in range(2000):
    if i < 1000:
        ans_list.append(1)
    else:
        ans_list.append(1000)

# n 값에따라 결과 도출
if n < 1000:
    print(n)
    semi_ans_list = [1] * n
    for i in semi_ans_list:
        print(i, end=' ')
elif n == 1000000:
    print(1999)
    for i in range(1000):
        print(1, end=' ')
    for i in range(999):
        print(1000, end=' ')
elif n == 1000:
    print(1)
    print(1000)
else: # n이 1000보다 클 때 -> 1000으로 나눈 몫만큼 1000을 뒤에 써주고, 나머지만큼 1을 앞에 써주자
    cnt_1000 = n // 1000
    cnt_1 = n % 1000
    semi_ans_list = [1] * cnt_1 + [1000] * cnt_1000
    print(len(semi_ans_list))
    for i in semi_ans_list:
        print(i, end=' ')