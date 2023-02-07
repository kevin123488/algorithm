import sys
sys.stdin = open('11650input.txt')

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    # xi, yi 위치가 주어짐
    xi, yi = map(int, sys.stdin.readline().split())
    arr.append([xi, yi])

# 버블정렬 써보자
arr.sort()
for i in arr:
    print(i[0], end=' ')
    print(i[1])