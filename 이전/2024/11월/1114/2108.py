import sys
sys.stdin = open('input_2108.txt')
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

n = int(input())
san_pyung = 0
joong = 0
choi_bean = 0
range_ans = 0
num_list = list(int(input()) for _ in range(n))
num_list.sort()

# 산술평균
san_pyung = sum(num_list) / n

num_dict = {}
for i in num_list:
    try:
        num_dict[i] += 1
    except:
        num_dict[i] = 1

# 중앙값 -> 11개의 수가 있다면 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11 -> 6이 중앙값.
# n개의 수 중 중앙값은 num_list[n//2]

# 중앙값
choi_bean = num_list[n // 2]

# 최빈값
