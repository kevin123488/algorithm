import sys
sys.stdin = open('9095input.txt')

T = int(input())
arr = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0] # 인덱스에 해당하는 값을 만들기 위해 arr[idx]만큼 필요
for i in range(4, 12):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
for i in range(T):
    n = int(input())
    # n을 1, 2, 3의 합으로 나타내야 함
    # 총 몇 가지의 경우가 나올 수 있는지 확인
    # n개의 1을 몇 종류의 부분집합으로 나눌 수 있는가?
    print(arr[n])