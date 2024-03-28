import sys
from itertools import combinations, permutations
sys.stdin = open('input15654.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = list(permutations(arr, M))
for i in ans:
    for j in i:
        print(j, end=" ")
    print()