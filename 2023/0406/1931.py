import sys
sys.stdin = open('input1931.txt')
input = sys.stdin.readline

n = int(input())
# 한 개의 회의실
# N개의 회의에 대해 회의실 사용표를 만들려 함
# 각 회의 i에 대해 시작시간과 끝나는 시간이 주어져 있음
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([end, start])

# 각 회의가 겹치지 않으면서 회의의 갯수를 최대로 가져가보자.
# 회의는 한번 시작하면 중간에 중단될 수 없다. 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우 시작하자마자 끝나는 것으로 생각하면 된다.

arr.sort()
cnt = 0
before_end = 0 # 이전 회의가 끝난 시간
for i in range(len(arr)):
    arr[i] = [arr[i][1], arr[i][0]]
# print(arr)
for i in arr:
    if i[0] >= before_end:
        cnt += 1
        before_end = i[1]

print(cnt)