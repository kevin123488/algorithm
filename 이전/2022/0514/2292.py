import sys
sys.stdin = open('2292.txt')

# 육각형으로 이루어진 벌집
# 중앙 -> 1
# 그 아랫방부터 시계방향으로 1씩 증가하면서 들어감
# 반복
# 숫자 N이 주어짐
# 1번 방에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지 계산

N = int(sys.stdin.readline())
# 층으로 나누어서 생각하면 될듯
# 1 -> 1개
# 2 3 4 5 6 7 -> 6개
# 8 9 10 11 12 13 14 15 16 17 18 19 -> 12개
# 20 ~ 37개 -> 18개
# 1부터 N까지의 배열을 만들자
# 근데 그걸 층별로 쪼개서 배열당 한층씩 넣어보자

final_arr = [[1]]

i = 1
z = 1
if N == 1:
    print(1)
else:
    while z < N:
        z = final_arr[-1][-1]
        final_arr.append([z+1, z+6*i])
        if z+1 <= N <= z+6*i:
            print(i+1)
            break
        z = final_arr[-1][-1]
        i += 1