import sys
sys.stdin = open('1018_input.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
ans1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
ans2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# 세로 N, 가로 M 사이즈의 판을 8*8로 잘라서 확인해야 함
# 바꿔야 하는 칸의 수를 최소로 만들어야 함
# 이중포문을 돌아야 한다. 그때의 range 범위를 조절해보자
a = 0
b = 0
cnt1 = 0
cnt2 = 0
ans_list = [] # 여기 고쳐야 하는 칸의 수를 저장할 예정
for i in range(a, a+8):
    for j in range(b, b+8):
        # 해당 이차원 리스트를 조회하자
        # 그 과정에서 리스트의 시작점과 끝점을 확인해주자
        for k in range(8):
            for z in range(8):
                if ans1[k][z] != arr[i][j]:
                    cnt1 += 1
                if ans2[k][z] != arr[i][j]:
                    cnt2 += 1
ans_list.append(cnt1)
ans_list.append(cnt2)
print(ans_list)