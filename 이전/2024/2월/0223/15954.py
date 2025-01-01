import sys
import decimal
sys.stdin = open('15954.txt')

def find_v(list):
    ans = 0
    m = sum(list) / len(list)
    for i in list:
        ans += (i - m) ** 2

    ans /= len(list)

    std_dev = decimal.Decimal(ans).sqrt()
    return std_dev

def find_ans(j):
    min_std_dev = float('inf')
    for i in range(len(int_list) - j + 1):
        sub_array = int_list[i:i+j]
        std_dev = find_v(sub_array)
        min_std_dev = min(min_std_dev, std_dev)
    return min_std_dev
    

N, K = map(int, input().split())
int_list = list(map(int, input().split()))
int_list.sort()

decimal.getcontext().prec = 28  # 28자리까지 정확한 연산을 수행하도록 설정

# N: 인형의 종류
# 선호도 비슷한 인형끼리 가깝게 위치하도록 서로 다른 N개의 인형을 배치
# 선호하는 사름의 수의 표준편차가 최소가 되는 K개 이상의 연속된 위치에 있는 인형들을 선택하여 같은 곳에 배치

# 1, 2, 5, 3, 4 이렇게 수가 입력되면 1, 2, 3, 4, 5로 정렬할 수 있다
# 정렬된 수는 123, 234, 345 이렇게 나눌 수 있고, 그 중 가장 표준편차값이 적은 값을 찾아 출력하면 된다.

real_ans = 1000000000
for i in range(K, N + 1):
    real_ans = min(real_ans, round(find_ans(i), 12))

print(real_ans)