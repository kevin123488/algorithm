import sys
sys.stdin = open('2116.txt')

N = int(input()) # 주사위의 개수
arr = [list(map(int, input().split())) for _ in range(N)] # 주사위 각 면의 숫자 정보

max_list = []
for i in range(6):
    max_ans = 0
    max_ans += max(arr[0][1], arr[0][2], arr[0][3], arr[0][4])
    a = arr[1].index(arr[0][5])
