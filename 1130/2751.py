# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 
# 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
import sys
sys.stdin = open('2751input.txt')
# sys.setrecursionlimit(100000)

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2] # 어디로 잡든 크게 상관 없었던 것 같음
#     small, middle, large = [], [], []
#     for i in arr:
#         if i < pivot:
#             small.append(i)
#         elif i > pivot:
#             large.append(i)
#         else:
#             middle.append(i)
    
#     return quick_sort(small) + middle + quick_sort(large)

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
    print(i)