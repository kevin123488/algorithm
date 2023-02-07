import sys
sys.stdin = open('1083input.txt')
sys.setrecursionlimit(100000)

# 크기가 N인 배열 A가 있다. 배열에 있는 모든 수는 서로 다르다.
# 이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다.
# 그리고, 교환은 많아봐야 S번 할 수 있다. 이때, 소트한 결과가 사전순으로 가장 뒷서는 것을 출력한다.
# S번 소트해서 사전순으로 가장 뒤에 있는 결과물을 출력하면 되는 문제(앞에 큰 숫자가 오면 됨)

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# S번 실행할것
# 2개 단위로 숫자를 비교. 큰 숫자가 앞에 있으면 S를 소비할 필요가 없음
# 우선 최악의 상황을 가정하고, S번의 기회가 있으면 몇번째까지의 숫자를 커버할 수 있는지 확인하자.
# 1 2 3, S = 2일 떄, 3개까지의 숫자를 커버할 수 있다. 인덱스 S까지 커버 가능하다고 생각하자.
# 인덱스 S와 받은 배열의 길이를 비교하자
# 인덱스 S 내의 숫자중 가장 큰 값을 선택, 그 위치를 받아 걔를 가장 앞으로 옮겨보자. 그리고 그 때 사용한 이동횟수만큼
# S에서 차감하면 된다.
start = 0 # 조회할 부분의 시작점
while S > 0:
    check_arr = arr[start:S + 1]
    idx = check_arr.index(max(check_arr))
    print(idx)

for i in arr:
    print(i, end=' ')