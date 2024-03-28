import sys
sys.stdin = open('input13262.txt')

# 해당 풀이는 그리디. 이 방식으로 풀 경우
# 1
# 5 5
# 1 2
# 2 3
# 3 4
# 4 5
# 5 1
# 위와 같은 입력이 들어올 경우 possible을 출력하게 됨. 잘못된 풀이

def find_ans(find):
    # find = [1, 3, 4]
    # 2번과 1, 3, 4가 연결되어 있다. 1, 3, 4가 서로 연결되어 있는지 아닌지를 판별해야 한다.
    for i in range(len(find)):
        check = find[i]
        for j in range(len(find)):
            if i == j:
                pass
            else:
                if check in arr[find[j]]:
                    print('impossible')
                    return 0

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)] # 인접리스트 사용
    for i in range(m):
        idx, rnd = map(int, input().split())
        arr[idx].append(rnd)
        arr[rnd].append(idx)
        # [1, 2]가 입력되었다면, 동그라미 1과 동그라미 2가 직선으로 서로 연결되었다는 것.

    # 동그라미와 동그라미 두 개를 연결하는 직선들 만으로 그림을 그리고, 연결된 두 동그라미는 색이 다르게 되도럭 칠하고자 한다.
    # 두가지 색상으로 칠하는 것이 가능한지 아닌지 판별하자

    # 1 2
    # 2 3
    # 3 4
    # 1 3
    # 2 4

    # 두 가지 색으로 칠하기 위해선 -> a 동그라미와 연결된 b 동그라미가 있다. 그 b 동그라미와 연결된 동그라미 중 a 동그라미에
    # 연결된 동그라미가 없어야 한다.
    # 즉, 특정 동그라미와 연결된 두 동그라미가 서로 연결되어 있으면 안된다.
    # 인접리스트 순회, 한 차원 안으로 들어간 요소들끼리 연결되어 있는지 아닌지 판독하자.
    flag = 1
    for i in range(1, len(arr)): # arr의 길이는 n보다 1 큼. 즉 n까지 순회. 인덱스 == 조회중인 동그라미 번호
        # 조회중인 리스트 내부의 값들이 연결되어 있는지 아닌지를 판별해야 함
        if find_ans(arr[i]) == 0:
            flag = 0
            break

    if flag == 1:
        print('possible')