import sys
sys.stdin = open('2842input.txt')

N = int(input())

# 상덕이는 언덕 위에 있는 마을의 우체국에 직업을 얻었다. 마을은 N×N 행렬로 나타낼 수 있다.
# 행렬로 나뉘어진 각 지역은 우체국은 'P', 집은 'K', 목초지는 '.' 중 하나로 나타낼 수 있다. 또, 각 지역의 고도도 알고 있다.
# 매일 아침 상덕이는 마을의 모든 집에 우편을 배달해야 한다. 배달은 마을에 하나밖에 없는 우체국 'P'가 있는 곳에서 시작한다.
# 상덕이는 현재 있는 칸과 수평, 수직, 대각선으로 인접한 칸으로 이동할 수 있다. 마지막 편지를 배달하고 난 이후에는 다시 우체국으로 돌아와야 한다.
# 상덕이는 이렇게 매일 아침 배달을 하는 것이 얼마나 힘든지 궁금해졌다. 상덕이가 배달하면서 방문한 칸 중 가장 높은 곳과 낮은 곳의 고도 차이를 피로도라고 하자.
# 이때, 가장 작은 피로도로 모든 집에 배달을 하려면 어떻게 해야 하는지 구하는 프로그램을 작성하시오.

# 그래프를 탐색하며 가장 높은 고도와 가장 낮은 고도를 체크할 필요가 있음
# P 지점을 출발점으로 잡을 필요가 있음

start_point = [] # P의 위치 저장
house_point = []
road_map = []
height_map = []
for i in range(N):
    road = list(input())
    for j in range(len(road)):
        if road[j] == 'P':
            start_point = [i, j]
        elif road[j] == 'K':
            house_point.append([i, j])

for i in range(N):
    height_map.append(list(map(int, input().split())))

# 완전탐색이 불가능한 이유: 방문한 곳을 또 방문할 수 있기 때문에, 무한루프를 돌 가능성이 높음
# 반드시 거쳐야 하는 지점: P, K의 위치. 그러므로 해당 위치의 고도는 반드시 저장할 필요가 있음.