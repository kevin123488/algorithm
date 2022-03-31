import sys
sys.stdin = open('2477.txt')

N = int(input()) # 1m^2에서 재배할 수 있는 참외의 수
# 동, 서, 남, 북 쪽으로 1, 2, 3, 4
arr = [list(map(int, input().split())) for _ in range(6)] # 배열대로 이동한다고 보면 됨. 예를 들어 [4, 20]의 경우
# 반시계 방향으로 돌고 있고 돌고있는 모양 또한 정해져 있으므로, 가능항 방향의 가짓수는 정해져있음
# 24가지만 잡아주면... 될듯

# 방향을 받아두는 리스트를 만들자
where_list = []
range_list = []
for i in arr:
    where_list += [i[0]]
    range_list += [i[1]]
if where_list == [4, 2, 3, 1, 3, 1]:
    ans = range_list[0]*range_list[1] - range_list[3]*range_list[4]
elif where_list == [4, 2, 3, 1 , 4, 1]:
    ans = range_list[1]*range_list[2] - range_list[4]*range_list[5]
elif where_list == [4, 2, 4, 2, 3, 1]:
    ans = range_list[4]*range_list[5] - range_list[1]*range_list[2]
elif where_list == [4, 2, 3, 2, 3, 1]:
    ans = range_list[0]*range_list[5] - range_list[3]*range_list[2]
elif where_list == [2, 3, 1, 3, 1, 4]:
    ans = range_list[0]*range_list[5] - range_list[2]*range_list[3]
elif where_list == [2, 3, 1, 4, 1, 4]:
    ans = range_list[0]*range_list[1] - range_list[3]*range_list[4]
elif where_list == [2, 4, 2, 3, 1, 4]:
    ans = range_list[3]*range_list[4] - range_list[0]*range_list[1]
elif where_list == [2, 3, 2, 3, 1, 4]:
    ans = range_list[4]*range_list[5] - range_list[1]*range_list[2]
elif where_list == [3, 1, 3, 1, 4, 2]:
    ans = range_list[4]*range_list[5] - range_list[1]*range_list[2]
elif where_list == [3, 1, 4, 1, 4, 2]:
    ans = range_list[0]*range_list[5] - range_list[2]*range_list[3]
elif where_list == [4, 2, 3, 1, 4, 2]:
    ans = range_list[2]*range_list[3] - range_list[0]*range_list[5]
elif where_list == [3, 2, 3, 1, 4, 2]:
    ans = range_list[3]*range_list[4] - range_list[0]*range_list[1]
elif where_list == [1, 3, 1, 4, 2, 3]:
    ans = range_list[3]*range_list[4] - range_list[0]*range_list[1]
elif where_list == [1, 4, 1, 4, 2, 3]:
    ans = range_list[4]*range_list[5] - range_list[1]*range_list[2]
elif where_list == [2, 3, 1, 4, 2, 4]:
    ans = range_list[1]*range_list[2] - range_list[4]*range_list[5]
elif where_list == [2, 3, 1, 4, 2, 3]:
    ans = range_list[2]*range_list[3] - range_list[0]*range_list[5]
elif where_list == [3, 1, 4, 2, 3, 1]:
    ans = range_list[2]*range_list[3] - range_list[0]*range_list[5]
elif where_list == [4, 1, 4, 2, 3, 1]:
    ans = range_list[3]*range_list[4] - range_list[0]*range_list[1]
elif where_list == [3, 1, 4, 2, 4, 2]:
    ans = range_list[0]*range_list[1] - range_list[3]*range_list[4]
elif where_list == [3, 1, 4, 2, 3, 2]:
    ans = range_list[1]*range_list[2] - range_list[4]*range_list[5]
elif where_list == [1, 4, 2, 3, 1, 3]:
    ans = range_list[1]*range_list[2] - range_list[4]*range_list[5]
elif where_list == [1, 4, 2, 3, 1, 4]:
    ans = range_list[2]*range_list[3] - range_list[0]*range_list[5]
elif where_list == [1, 4, 2, 4, 2, 3]:
    ans = range_list[0]*range_list[5] - range_list[2]*range_list[3]
else:
    ans = range_list[0]*range_list[1] - range_list[3]*range_list[4]

real_ans = ans*N
print(real_ans)