import sys
sys.stdin = open('15649input.txt')
from itertools import combinations, permutations
N, M = map(int, input().split())
arr = []
for i in range(1, N+1):
    arr.append(i)
ans_list = list(permutations(arr, M))
for i in ans_list:
    for k in i:
        print(k, end=" ")
    print()