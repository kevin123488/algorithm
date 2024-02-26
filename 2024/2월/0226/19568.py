ans_list = [[0] * 30 for _ in range(30)]

# 이거 1, 10, 100, 1000 조합하면 되는거 아님?
# 15, 15, 15, 15 -> 최대 15000 + @ 밖에 안됨
# 모든 수가 되어야하므로 1씩 증가하는 부분은 반드시 있어야 함
# 1, 20, 400, 8000 -> X
# 15를 기준으로 해야 다음 단계(1 -> 15, 15 -> 225)로 넘어갈 때 까지 나오는 모든 수를 구할 수 있음.
# 15진수 생각하면 됨

for i in range(30):
    for j in range(30):
        if i == 15 and j == 15:
            ans_list[i][j] = 0
        elif i == 15:
            if j > 15:
                ans_list[i][j] = 15*15*15
            else:
                ans_list[i][j] = 1
        elif j == 15:
            if i > 15:
                ans_list[i][j] = 15
            else:
                ans_list[i][j] = 15*15

cnt = 0
for i in range(30):
    for j in range(30):
        cnt += 1
        print(ans_list[i][j], end=' ')
        if cnt == 30:
            print()
            cnt = 0