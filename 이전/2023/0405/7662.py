import sys
import heapq
sys.stdin = open('input7662.txt')
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    k = int(input())
    min_q = []
    max_q = []
    heapq.heapify(min_q)
    heapq.heapify(max_q)
    cnt = 0
    # I n -> n을 q에 삽입
    # D 1 -> q에서 최댓값 삭제
    # D -1 -> q에서 최솟값 삭제
    # q가 비어있다면 D연산 무시 가능
    for i in range(k):
        do = input().strip()
        if do[0] == 'I':
            cnt += 1
            heapq.heappush(min_q, int(do[2:]))
            heapq.heappush(max_q, -1 * int(do[2:]))
        else:
            if cnt == 0:
                pass
            else:
                cnt -= 1
                if do[2] == '-':
                    heapq.heappop(min_q) # 최솟값 삭제
                else:
                    heapq.heappop(max_q) # 최댓값 삭제

    if cnt == 0:
        print('EMPTY')
    else:
        print(-1 * min(max_q), min(min_q))