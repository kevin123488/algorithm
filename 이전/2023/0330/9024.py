import sys
sys.stdin = open('input9024.txt')
input = sys.stdin.readline

# 여러개의 서로 다른 정수 S와 또 다른 정수 K가 주어짐. S에 속하는 서로 다른 두 개의 정수의 합이 K에 가장 가까운
# 두 정수를 구하자. 그 두 정수의 조합의 수를 출력하자.
# ex) S = [1, 2, 3, 5, 6, 7, 8, 10], k = 11
# (5, 6), (3, 8), (1, 10) -> 3

# t = int(input())
# for tc in range(t):
#     n, k = map(int, input().split())
#     s = list(map(int, input().split()))
#     johap_list = []
#     max_ans = 2 * 10 ** 8
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if abs(k - (s[i] + s[j])) < max_ans:
#                 johap_list = [[s[i], s[j]]]
#                 max_ans = abs(k - (s[i] + s[j]))
#             elif abs(k - (s[i] + s[j])) == max_ans:
#                 johap_list.append([s[i], s[j]])
#
#     print(len(johap_list))

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    left, right = 0, n-1
    cnt = 0
    min_diff = float('inf')
    while left < right:
        temp_sum = s[left] + s[right]
        temp_diff = abs(k - temp_sum)
        if temp_diff < min_diff:
            min_diff = temp_diff
            cnt = 1
        elif temp_diff == min_diff:
            cnt += 1
        if temp_sum < k:
            left += 1
        else:
            right -= 1
    print(cnt)