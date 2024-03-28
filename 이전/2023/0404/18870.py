import sys
from copy import deepcopy
sys.stdin = open('input18870.txt')
input = sys.stdin.readline

n = int(input())
# 수직선 위에 n개의 좌표
# 좌표 압축 적용
# [a, b, c, d, e]가 있다. 이 좌표들을 좌표 압축해보자
# a좌표를 압축하면 해당 좌표 리스트에서 a보다 작은 좌표의 개수가 된다.
# [1, 2, 3, 4, 5]일 경우, 좌표 압축하면 [0, 1, 2, 3, 4]가 되는 것

arr = list(map(int, input().split()))
arr_2 = list(set(deepcopy(arr)))
arr_2.sort()
for i in arr:
    ans = 0
    # 이분 탐색 사용
    start = 0
    end = len(arr_2)
    while True:
        middle = (start + end) // 2
        if arr_2[middle] > i:
            # 찾고자 하는 값이 중간값보다 적다면 범위를 줄여줘야 함
            end = middle - 1
        elif arr_2[middle] < i:
            start = middle + 1
        else:
            print(middle, end=" ")
            break