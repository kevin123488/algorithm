import sys
import heapq
sys.stdin = open('input1927.txt')
input = sys.stdin.readline

n = int(input())
arr = []
heapq.heapify(arr)
for i in range(n):
    work = int(input())
    if work == 0:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, work)