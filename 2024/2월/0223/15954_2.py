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

def find_ans(j, int_list, precalculated_std_dev):
    min_std_dev = float('inf')
    for i in range(len(int_list) - j + 1):
        if i == 0:
            std_dev = precalculated_std_dev[j-1][i]
        else:
            std_dev = precalculated_std_dev[j-1][i] - ((int_list[i-1] - int_list[i+j-1]) ** 2 - (int_list[i+j-1] - int_list[i+j]) ** 2) / j
        min_std_dev = min(min_std_dev, std_dev)
        precalculated_std_dev[j-1][i] = std_dev
    return min_std_dev

N, K = map(int, input().split())
int_list = list(map(int, input().split()))
int_list.sort()

decimal.getcontext().prec = 28  # 28자리까지 정확한 연산을 수행하도록 설정

# 미리 부분 리스트의 표준 편차를 계산하여 저장
precalculated_std_dev = [[0] * (N-K+1) for _ in range(K)]  # 수정된 부분
for j in range(1, K+1):
    for i in range(len(int_list) - j + 1):
        sub_array = int_list[i:i+j]
        precalculated_std_dev[j-1][i] = find_v(sub_array)

# 최소 표준 편차 계산 및 출력
real_ans = float('inf')
for i in range(K, N + 1):
    real_ans = min(real_ans, round(find_ans(i, int_list, precalculated_std_dev), 12))

print(real_ans)