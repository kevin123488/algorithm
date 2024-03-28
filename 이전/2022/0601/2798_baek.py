import sys
sys.stdin = open('2798_input.txt')

def dfs(i, max_ans, how_plus):
    global M, ans

    if how_plus == 3:
        if ans <= max_ans <= M:
            ans = max_ans
            return

    if max_ans > M:
        return


    for z in range(len(card_num)):
        if visited[z] == 0 and how_plus < 3:
            visited[z] = 1
            dfs(z, max_ans+card_num[z], how_plus+1)
            visited[z] = 0

N, M = map(int, input().split()) # N: 카드의 개수, M: 카드3장의 합이 M을 넘지 않는 조합 중 가장 큰 값을 찾아야 함
card_num = list(map(int, input().split()))

# sub_set = [[]]
# max = 0
# for i in card_num:
#     a = len(sub_set)
#     for j in range(a):
#         list_set = [i] + sub_set[j]
#         print(list_set)
#         sub_set.append([i] + sub_set[j])
#         if len(list_set) == 3:
#             if max <= sum(list_set) <= M:
#                 max = sum(list_set)
#
# print(max)

# 위의 방법은 메모리 초과가 난다. 그렇다면? dfs로 해보자
# dfs는 시간초과가 뜬다
visited = [0 for _ in range(N)]
max_ans = 0
how_plus = 0
ans = 0
dfs(0, 0, 0)
print(ans)