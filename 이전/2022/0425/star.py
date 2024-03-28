# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# N = int(input())
# for i in range(1, N+1):
#     ans = '*'*i
#     print(ans)

# 9개의 서로 다른 자연수가 입력됨(한줄에 하나씩)
# arr = []
# for i in range(9):
#     arr.append(int(input()))
#
# ans_list = []
# ans = 0
# for k in range(len(arr)):
#     if arr[k] > ans:
#         ans = arr[k]
#         ans_list.append((ans, k+1))
#
# print(ans_list[-1][0])
# print(ans_list[-1][1])

# arr = list(map(int, input().split()))
# if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
#     print('ascending')
# elif arr == [8, 7, 6, 5, 4, 3, 2, 1]:
#     print('descending')
# else:
#     print('mixed')