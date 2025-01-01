import sys
sys.stdin = open('17404.txt')
sys.setrecursionlimit(100000)

def dfs(n, now_house_idx, now_color, first_color, now_spent):
    # 집의 수, 현재 탐색 완료한 집의 인덱스, 방금 탐색한 집에서 선택한 색상, 첫번째로 선택한 색상, 지금까지 소비한 금액
    global ans
    
    if now_spent > ans: # 유망하지 않은 루트
        return

    if now_house_idx == -1: # 아직 어떤 집도 탐색하지 않음
        if ans > house[0][0]:
            dfs(n, 0, 0, 0, house[0][0])
        if ans > house[0][1]:
            dfs(n, 0, 1, 1, house[0][1])
        if ans > house[0][2]:
            dfs(n, 0, 2, 2, house[0][2])

    elif 0 <= now_house_idx < n - 2:
        for color in range(3):
            if color != now_color and now_spent + house[now_house_idx + 1][color] < ans:
                dfs(n, now_house_idx + 1, color, first_color, now_spent + house[now_house_idx + 1][color])
    
    elif now_house_idx == n - 2: # 마지막 집까지 모두 탐색했을 때
        for color in range(3):
            if color != now_color and color != first_color and now_spent + house[now_house_idx + 1][color] < ans:
                dfs(n, now_house_idx + 1, color, first_color, now_spent + house[now_house_idx + 1][color])
        
    else: # 마지막 집까지 모두 탐색했을 때
        if ans > now_spent:
            ans = now_spent
            return

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)] # 각 집을 빨, 초, 파로 칠하는 비용

# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

# 요약
# 연속된 집의 경우 색이 달라야 함
# 1번과 n번의 집의 색은 달라야 함

# 가능한 모든 케이스를 확인한 후 비용의 합을 비교하여 최솟값을 리턴하자
ans_list = []

# dfs 및 백트래킹 사용
visited = [-1] * n
ans = 1000009
# dfs를 수행할 때 첫번째 집의 색과 직전에 선택한 색의 정보를 넘겨주자
dfs(n, -1, -1, -1, 0) # 색은 0 -> 빨, 1 -> 초, 2 -> 파.

# print(visited)
print(ans)