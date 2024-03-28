import sys
sys.stdin = open('2164input.txt')
from collections import deque

# def find_ans(arr):
#     # print(arr)
#     if len(arr) == 1:
#         print(arr[0])
#         return
#     elif len(arr) > 1:
#         arr.pop(0)
#         # print(arr)
#         if len(arr) == 1: # 4
#             print(arr[0])
#             return
#         elif len(arr) > 1: # 2345 452 24
#             k = arr.pop(0) # 2 4 2
#             arr.append(k) # 3452 524 42
#             find_ans(arr)

N = int(input())

# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 
# 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 
# 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 
# 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 1부터 입력받은 숫자까지의 수를 리스트에 넣을 필요가 있음
arr = deque()
for i in range(1, N+1):
    arr.append(i)
# 전체 갯수 체크, 1개? -> 출력, 아니다?
# 제일 첫 숫자는 버림, 버린 후 전체 갯수 체크, 1개? -> 출력
# 1개 아니다? 첫 숫자 버린 후의 리스트에서 첫 숫자를 골라 제일 뒤로 보냄
# find_ans(arr)

# 재귀 안쓰는 방법
# 카드 개수 N개
# 사이클 N-1번
# 마지막에 남는 카드는?

while len(arr) > 1:
    arr.popleft()
    pop_left = arr.popleft()
    arr.append(pop_left)
    
print(arr[0])