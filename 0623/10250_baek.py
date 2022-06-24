import sys
sys.stdin = open('10250_input.txt')

# 손님이 도착하는대로 방을 배정함
# 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 함
# 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하자
# 각 층에 W개의 방이 있는 H층 건물이라고 함 (1 <= H, W <= 99)
# 엘리베이터는 가장 왼쪽에 있음
# 방 번호는 YXX, YYXX의 형태로 주어짐. Y 또는 YY의 경우 층 수를, XX는 앨리베이터에서 세었을 때의 번호를 나타냄
# 엘베타고 이동하는 거리는 고려하지 않음. 그러나 걷는 거리가 같다면, 낮은 층의 방을 선호함
# 모든 방이 비어있다고 가정. N번째 손님에게 배정될 방은?

T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())

    # 채워지는 순서: 101, 201, ... , H01, ... 102, 202, ... , H02, ... , ... ,
    # cnt 하면서 채워보자
    cnt = 0
    flag = 0
    for i in range(1, W+1):
        if flag:
            break
        for j in range(1, H+1):
            cnt += 1
            if cnt == N:
                # print(i, j)
                floor = j
                room = i
                flag = 1
                break
    ans = []
    if room < 10:
        ans.append(floor)
        ans.append(0)
        ans.append(room)
    else:
        ans.append(floor)
        ans.append(room)

    for i in ans:
        print(i, end='')
    print()