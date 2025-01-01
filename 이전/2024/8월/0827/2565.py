import sys
sys.stdin = open('2565.txt')
from pprint import pprint

n = int(input())
link_list = [list(map(int, input().split())) for _ in range(n)]

# 전깃줄이 교차하는 경우가 있다. 몇 개의 줄을 없애 전깃줄이 교차하지 않도록 하려 한다.
# 전깃줄이 교차하지 않기 위한 조건은?
# a선 기준으로 오름차순 정렬 후 선을 쭉 그었을 때 그 어떤 선의 b 값도 이전 선의 b 값보다 적으면 안됨

link_list.sort()
print(link_list)
# 칸별로 교차하는 선분의 정보를 입력하자. 진입차수 개념으로 봐도 될 듯 하다.
# 한 선분씩 없애 보며 모든 선분이 삭제되는 순간을 체크해보자

cross_line = [0] * n
cross_line_check = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 기준선
        now_point_start = link_list[i][0]
        now_point_fin = link_list[i][1]
        if i != j:
            # 교차 판별 선
            start_point = link_list[j][0]
            fin_point = link_list[j][1]

            if now_point_start < start_point and now_point_fin > fin_point:
                cross_line[i] += 1
                cross_line_check[i][j] = 1
            elif now_point_start > start_point and now_point_fin < fin_point:
                cross_line[i] += 1
                cross_line_check[i][j] = 1

print(cross_line)
pprint(cross_line_check) # cross_line_check[i] -> i번째 선에 대해 교차하고있는 선에 대해 1의 값을 넣어줌
# 완탐으로 모든 케이스를 삭제해가며
# cross_line_check의 1의 개수가 0이 되기 위한 최소 트라이 횟수를 체크하면 될 것 같음

all_cross = sum(cross_line) // 2
print(all_cross)