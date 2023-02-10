import sys
from itertools import combinations
from copy import deepcopy
sys.stdin = open('15686input.txt')

def find_least_chicken(i, j): # 집 좌표
    global copy_city
    ans = 10000000
    for k in range(N):
        for z in range(N):
            if copy_city[k][z] == 2 and abs(k-i) + abs(z-j) < ans:
                ans = abs(k-i) + abs(z-j)

    return ans # 집 하나에 대한 치킨 거리

def find_ans(list):
    global real_ans
    # 받은 도시의 이차원 배열을 이용, 치킨거리를 구하는 함수.
    ans = 0
    for i in range(N):
        for j in range(N):
            if list[i][j] == 1:
                ans += find_least_chicken(i, j) # 집 좌표 하나에 대한 치킨 거리를 ans에 더해주자
                if ans >= real_ans: # 그러다 현재 저장되어 있는 real_ans보다 커지는 순간
                    return real_ans # 유망성 없으므로 가지치기
    real_ans = ans

def find_chicken_length(list): # list는 ([0, 1], [1, 1], [2, 1], [3, 1])와 같은 형태.
    global real_ans
    global copy_city
    # list에는 폐쇄해야 되는 치킨집의 리스트가 적혀 있다.
    for i in list:
        try:
            copy_city[i[0]][i[1]] = 0
        except:
            pass
    find_ans(copy_city) # 폐쇄지점 골라서 뽑아봄
    copy_city = deepcopy(city)


N, M = map(int, input().split())
# 도시의 치킨집 중 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
# 도시의 치킨 거리가 가장 작게 되는 경우를 구하시오.
# 치킨 거리가 적으려면, 많은 치킨집이 있어야 유리하다. 그러므로 M개의 치킨집을 고르는 방향으로 가도록 하자.

city = []
for i in range(N):
    city.append(list(map(int, input().split())))

chicken_list = []
# 조합을 활용, 폐쇄할 치킨집을 골라 보자.
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_list.append([i, j])

# if M == 1:
#     find_chicken_list = chicken_list
# else:
#     find_chicken_list = list(combinations(chicken_list, M))
find_chicken_list = list(combinations(chicken_list, len(chicken_list) - M)) # 폐쇄 목록
# [([0, 1], [1, 1], [2, 1], [3, 1]), ([0, 1], [1, 1], [2, 1], [4, 1]), ([0, 1], [1, 1], [3, 1], [4, 1]), ([0, 1], [2, 1], [3, 1], [4, 1]), ([1, 1], [2, 1], [3, 1], [4, 1])]

# find_chicken_list 순회하며 치킨집을 살려보자.
# 살아있는 치킨집에 대해 해당 도시의 치킨 거리를 구하자.
# 현재 계산중인 치킨 거리가 만약 기존의 치킨 거리보다 길어지는 순간이 있다면? 가지치키

real_ans = 100000000
copy_city = deepcopy(city)
if len(find_chicken_list) == 1 and find_chicken_list[0]:
    find_ans(copy_city)
else:
    for i in range(len(find_chicken_list)):
        find_chicken_length(find_chicken_list[i])
print(real_ans)