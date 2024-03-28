import sys
import heapq
sys.stdin = open('input7662.txt')
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    max_heap = []
    min_heap = []
    used = set()

    k = int(input())

    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == "I":
            heapq.heappush(max_heap, (-num, i))
            heapq.heappush(min_heap, (num, i))
            used.add(i)
        elif op == "D":
            if not used:
                continue

            if num == 1:
                while max_heap and max_heap[0][1] not in used:
                    heapq.heappop(max_heap)
                _, idx = heapq.heappop(max_heap)
            else:
                while min_heap and min_heap[0][1] not in used:
                    heapq.heappop(min_heap)
                _, idx = heapq.heappop(min_heap)

            used.remove(idx)

    while max_heap and max_heap[0][1] not in used:
        heapq.heappop(max_heap)
    while min_heap and min_heap[0][1] not in used:
        heapq.heappop(min_heap)

    if not used:
        print("EMPTY")
    else:
        max_val, _ = heapq.heappop(max_heap)
        min_val, _ = heapq.heappop(min_heap)
        print(-max_val, min_val)
