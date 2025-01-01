import sys
sys.stdin = open('2636.txt')
import pprint

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def is_it_hole(a, b): # a: 세로 인덱스, b: 가로 인덱스
    # 상, 하, 좌, 우로 쭉 이동했을 때 모두 1인 칸을 만날 수 있어야 구멍에 속하는 칸!
    # 1을 만나기 전에 no를 만나면 종료
    flag = 0 # no를 만나는 순간 1로 변경
    for i in range(4):
        if flag == 0:
            cnt = 0
            while True:
                na = di[i] * cnt + a
                nb = dj[i] * cnt + b
                if cheese[na][nb] == 'no':
                    flag = 1
                    break
                elif cheese[na][nb] == 1:
                    break
                cnt += 1
        else:
            break
    
    if flag == 0:
        return 'hole'
    else:
        return 'nohole'
    
    
def fill_hole(height, width): # 구멍인 칸을 채워 가장자리를 쉽게 판별 가능하게 해줌
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if cheese[i][j] == 0:
                find_hole = is_it_hole(i, j)
                if find_hole == 'hole':
                    cheese[i][j] = 2


def melting_cheese(height, width): # 치즈 녹이고, 해당 단계에서 몇개의 치즈가 녹았는지 확인
    cnt = 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if cheese[i][j] == 1 and (cheese[i + 1][j] == 0 or cheese[i - 1][j] == 0 or cheese[i][j + 1] == 0 or cheese[i][j - 1] == 0
                                      or cheese[i + 1][j] == 'no' or cheese[i - 1][j] == 'no' or cheese[i][j + 1] == 'no' or cheese[i][j - 1] == 'no'):
                cnt += 1
                cheese[i][j] = 3 # 녹은 치즈는 3으로 표시
    
    return cnt

def return_cheese(height, width): # 치즈를 녹인 후 2, 3가 되어있는 부분을 0으로 바꾸어줌
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if cheese[i][j] == 2 or cheese[i][j] == 3:
                cheese[i][j] = 0

height, width = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(height)]

# i = 0, -1, j = 0, -1인 부분엔 치즈가 들어갈 수 없음
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            cheese[i][j] = 'no'
        if j == 0 or j == width - 1:
            cheese[i][j] = 'no'

# 1로 채워져있는 칸은 치즈가 있는 칸
# 치즈 가장자리는 1시간이 지나면 녹음
# 치즈 구멍은 안녹음
# 치즈가 모두 녹아 없어지는데 필요한 시간과
# 모두 녹기 한시간 전에 남아있는 치즈조각의 수를 구하자
            
# 치즈의 구멍부분을 판별할 방법이 필요
            
# 비어있는 특정 칸에서 
# 쭉 올렸을 때, 내렸을 때, 오른쪽으로 보냈을 때, 왼쪽으로 보냈을 때 치즈가 있는 칸이 있을 경우
# 해당 칸은 구멍
# 구멍인 칸을 '임시로' 채운 후(다른 숫자로) 가장자리 판별
# (특정 칸과 인접한 빈 칸이 있을 경우 해당 칸은 가장자리)
# 가장자리 0으로 바꿔주고, 임시로 채운 칸 0으로 바꿔줌

cnt_list = []

while True:
    fill_hole(height, width)
    now_cnt = melting_cheese(height, width)
    return_cheese(height, width)
    if now_cnt == 0:
        break
    else:
        cnt_list.append(now_cnt)
    pprint.pprint(cheese)
    print()


print(len(cnt_list), cnt_list[-1])
print(cnt_list)

# 구멍인지 아닌지 판별하는 함수를 다시 짜야함.
# 값이 0인 칸에서 시작하는 탐색함수를 짜자. 탐색을 모두 돈 후 탐색 돈 칸에 대해 no와 인접한 칸이 있을 경우
# 해당 탐색돈 대상은 구멍이 아님
# 기존 fill_hole 함수의 형태를 살짝 바꿔서
# 매 단계마다 모든 0에 대해 탐색을 돌게 하자.