import sys
sys.stdin = open('naksi.txt')

# seat_isntfull 초기화 함수
def cho():
    global seat_isntfull
    seat_isntfull = []
    for i in range(1, N+1):
        seat_isntfull += [i]
    return seat_isntfull

# 밑에 설명해둔 함수
def howlong(a):
    cnt = 0
    global seat_isntfull
    # a[0]: 입구의 위치
    # a[1]: 해당 입구에 대기중인 낚시꾼의 수
    s = a[0]
    if s in seat_isntfull:
        seat_isntfull[seat_isntfull.index(s)] = 0
        cnt += 1
        s = a[0] + 1
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 낚시터 자리의 개수
    gate_1 = list(map(int, input().split())) # 입구 1의 정보
    gate_2 = list(map(int, input().split())) # 입구 2의 정보
    gate_3 = list(map(int, input().split())) # 입구 3의 정보

    # gate에 입구들의 위치와, 해당 입구에서 대기중인 낚시꾼의 수를 저장하였다.
    # 낚시꾼들의 입장에 필요한 이동거리에 영향을 끼치는 것은? 1. 입장 게이트의 순서, 2. 낚시꾼들이 들어갈 때 어느 자리를 고르는가?
    # 가장 가까운 곳을 고른다는 로직이 있긴 하지만, 마지막에 들어가는 낚시꾼의 경우 가장 가까운 거리가 2 곳 있다면? 어떻게 해야하는가?
    # 아마 다음 게이트와 먼 곳을 고르는 것이 옳을 것이다.
    # 일단 낚시꾼의 자리를 리스트로 만들어보자.
    seat = [0] * N
    seat_isntfull = []
    for i in range(1, N+1):
        seat_isntfull += [i]
    # seat_isntfull 리스트에 아직 차지되지 않은 자리의 인덱스를 넣어두었다.
    # 게이트의 시작 위치와 낚시꾼의 수를 받아 자리이동의 수를 계산하는 함수 howlong(a)를 만들자
    a = howlong(gate_1) + howlong(gate_2) + howlong(gate_3)
    cho()
    b = howlong(gate_1) + howlong(gate_3) + howlong(gate_2)
    cho()
    c = howlong(gate_2) + howlong(gate_1) + howlong(gate_3)
    cho()
    d = howlong(gate_2) + howlong(gate_3) + howlong(gate_1)
    cho()
    e = howlong(gate_3) + howlong(gate_1) + howlong(gate_2)
    cho()
    f = howlong(gate_3) + howlong(gate_2) + howlong(gate_1)

    ans = max(a, b, c, d, e, f)
    print(f'#{tc} {ans}')