import sys
sys.stdin = open('1920_input.txt')

# N개의 정수가 주어져있을 때, X라는 정수가 해당 정수들에 포함되어있는지 알아보자
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr_list = list(map(int, sys.stdin.readline().split()))
arr.sort() # 얘를 정렬해둬야 함
for i in range(M):
    # 이진탐색을 할 것
    start = 0 # 인덱스 기준으로 넣음
    end = len(arr) - 1
    flag = 0
    while start <= end: # 시작, 중간, 끝점을 수정해가며 조회범위를 절반씩 줄이는 것
        # 먼저 값을 비교해보자
        # 탐색 대상의 중간값과 찾고자 하는 값을 비교
        middle = (start + end) // 2
        if arr[middle] > arr_list[i]: # 만약 탐색대상 리스트의 가운데 값이 찾고자 하는 값보다 크면? 조회의 범위를 바꿔줘야겠지
            end = middle - 1
        elif arr[middle] == arr_list[i]: # 중간값과 같으면?
            print(1)
            flag = 1
            break
        elif start == end: # start와 end값이 같아 arr에 1개의 값만이 조회 가능한데 첫번째 elif에 걸리지 않았다? -> 값이 없다
            print(0)
            flag = 1
            break
        elif arr[middle] < arr_list[i]: # 가운데 값이 찾고자 하는 값보다 작으면?
            start = middle + 1
    if flag:
        pass
    else:
        print(0)