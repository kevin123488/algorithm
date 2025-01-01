import sys
sys.stdin = open('20040.txt')

def find_cycle(n, m):
    # 사이클 판별 방법
    # 조상 노드가 동일한지 확인
    print(n, m)

# 선 홀수, 후 짝수
# 0 ~ n - 1 까지의 n개의 점이 주어짐. 이 중 어떤 세 점도 일직선 위에 놓이지 않음.
# 매 차례 각 플레이어는 두 점을 이음. 그려져있는 선분을 다시 그을 순 없고 다른 선분과 교차하는 것은 가능
# 처음으로 사이클이 완성되는 순간 게임 종료.
# 사이클 -> 사이클에 속한 임의의 선분 한 점에서 출발해 모든 선분을 한번씩만 지나고 출발점으로 돌아올 수 있는 것

# 게임의 진행 상황이 주어지면 몇 차례에서 사이클이 완성되었는지, 혹은 아직 게임이 진행중인지 판별하는 프로그램
# 주어진 선분을 모두 탐색하였는데 사이클이 없다 -> 0 출력

n, m = map(int, input().split()) # n: 점의 수, m: 그은 선분의 수
line_list = [list(map(int, input().split())) for _ in range(m)]

# print(n, m, line_list)
# 우선 사이클 판별부터 하자
link_list = [[] for _ in range(n)]
for i in range(m):
    start, fin = line_list[i]
    link_list[start].append(fin)
    link_list[fin].append(start)

    # 인접리스트 정보를 갱신한 후 사이클이 있는지 없는지 체크하자
    if find_cycle(n, m):
        print(i + 1)
        break

print(link_list)