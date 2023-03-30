import sys
sys.stdin = open('input1504.txt')
input = sys.stdin.readline
import heapq


def bfs(start, end):
    gan_list = [10 ** 10] * (N + 1)
    gan_list[0] = 0
    gan_list[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    # heapq를 활용, 가중치가 낮은 애부터 뽑아쓸 수 있다.
    while q:
        d, s = heapq.heappop(q)

        s_link = inj_list[s]
        if gan_list[s] < d:
            continue
        for i in range(len(s_link)):
            if gan_list[s_link[i][1]] > gan_list[s] + s_link[i][0]:
                gan_list[s_link[i][1]] = gan_list[s] + s_link[i][0]
                heapq.heappush(q, [gan_list[s_link[i][1]], s_link[i][1]])

        # for i in range(len(s_link)):
        #     if visited[s_link[i][1]] == 0:
        #         heapq.heappush(q, [gan_list[s_link[i][1]], s_link[i][1]])
    return gan_list[end]

def find_di():
    ans1 = bfs(1, v1)
    ans2 = bfs(v1, v2)
    ans3 = bfs(v2, N)
    return_1 = ans1 + ans2 + ans3
    ans4 = bfs(1, v2)
    if ans4 > return_1:
        return return_1
    ans5 = bfs(v2, v1)
    if ans4 + ans5 > return_1:
        return return_1
    ans6 = bfs(v1, N)
    return_2 = ans4 + ans5 + ans6
    return min(return_1, return_2)

N, E = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())

inj_list = [[] for _ in range(N + 1)]
for i in arr:
    inj_list[i[0]].append([i[2], i[1]])
    inj_list[i[1]].append([i[2], i[0]])

gan_list = [10**10] * (N + 1)
gan_list[0] = 0

result = find_di()
if result < 10**10:
    print(result)
else:
    print(-1)