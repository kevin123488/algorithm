import itertools
import sys
sys.stdin = open('input15666.txt')

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans_list = list(itertools.combinations_with_replacement(nums, M))
ans_list = sorted(list(set(ans_list)))
for i in ans_list:
    for j in i:
        print(j, end=" ")
    print()