import sys
sys.stdin = open('1018input.txt')

def check_arr_b(arr): # arr를 넣으면 해당 arr에서 몇 개의 칸이 새로 칠해져야 하는지를 확인하는 함수. 결과값을 ans_list에 담아야 함
    # 시작값이 B인 경우와 대조
    count = 0
    for i in range(8):
        for z in range(8):
            if not (i+z)%2: # i와 z의 합이 짝수일 때
                if arr[i][z] == 'B':
                    count += 1
            if (i+z)%2:
                if arr[i][z] == 'W':
                    count += 1
    ans_list.append(count)

# 00, 02, 04, 06
# 11, 13, 15, 17
#


def check_arr_w(arr):  # arr를 넣으면 해당 arr에서 몇 개의 칸이 새로 칠해져야 하는지를 확인하는 함수. 결과값을 ans_list에 담아야 함
    # 시작값이 W인 경우와 대조
    count = 0
    for i in range(8):
        for z in range(8):
            if not (i + z) % 2:  # i와 z의 합이 짝수일 때
                if arr[i][z] == 'W':
                    count += 1
            if (i + z) % 2:
                if arr[i][z] == 'B':
                    count += 1
    ans_list.append(count)

# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.보드가 체스판처럼 칠해져 있다는 보장이 없어서,
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 검, 흰이 번갈아서 칠해져있어야 한다? 8*8 사이즈만큼 잘라서 확인해보자.
# 확인 결과(몇 개의 칸이 새로 칠해져야 하는지)를 리스트에 담고, 최솟값을 출력하자.

ans_list = [] # 확인 결과 담을 리스트
# 어떻게 8*8씩 끊어서 순회할 것 인가?
# 시작점을 조절하면 될 것
# [0, 0] ~ [M-8, N-8]까지가 범위가 됨 -> [i, j]로 두자
# [i, j] ~ [i+7, j+7]까지가 범위임
# 범위별로 시작 W, 시작 B로 나눠 각각의 확인 결과를 ans_list에 추가해주자.

for i in range(N-8+1):
    for j in range(M-8+1):
        # 주어진 i와 j의 값을 바탕으로 [i, j] ~ [i+7, j+7]범위의 값을 떼네어 확인
        sliced_arr = [] # 떼어낸 체스판을 담을 리스트
        for k in range(8):
            sliced_list = [] # 이 리스트를 sliced_arr에 차곡차곡 쌓을 것
            for z in range(8):
                sliced_list.append(arr[i+k][j+z])
            sliced_arr.append(sliced_list)
        check_arr_b(sliced_arr)
        check_arr_w(sliced_arr)

print(min(ans_list))