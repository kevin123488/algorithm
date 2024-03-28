import sys
from itertools import permutations
sys.stdin = open('input15657.txt')
input = sys.stdin.readline

def check_in(a, b): # a가 b 안에 있는지 확인. 있으면 1, 없으면 0 return
    for i in b:
        cnt = 0
        for j in range(len(a)):
            if a[j] != i[j]:
                pass
            else:
                cnt += 1
        if cnt == len(a):
            return 1
    return 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# N개의 자연수 중 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨
# 고른 수열은 비내림차순
arr.sort()
ans_list = list(permutations(arr, M))
# real_ans_list = []
# for i in range(len(ans_list)):
#     if i == 0:
#         real_ans_list.append(ans_list[i])
#     else:
#         if not check_in(ans_list[i], real_ans_list):
#             real_ans_list.append(ans_list[i])
#
# for i in real_ans_list:
#     for j in i:
#         print(j, end=" ")
#     print()
# print(ans_list)
ans_list = set(ans_list)
# print(ans_list)
ans_list = list(ans_list)
# print(ans_list)
ans_list.sort()
# print(ans_list)
for i in ans_list:
    for j in i:
        print(j, end=" ")
    print()