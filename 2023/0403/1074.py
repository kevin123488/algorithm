import sys
sys.stdin = open('input1074.txt')
input = sys.stdin.readline

def find_ans(n, r, c):
    if n == 0:
        return 0
    h = 2 ** (n - 1) # n이 3일 때 h는 4
    # 1, 2, 3, 4 사분면 중 어디에 위치하는지 확인
    # r의 범위는 4종류로 구분될 수 있음.
    # 1 사분면 -> r이 h보다 작아야 함, c가 h보다 작아야 함
    # 2 사분면 -> r이 h보다 작아야 함, c가 h보다 크거나 같아야 함
    # 3 사분면 -> r이 h 이상, c가 h 미만
    # 4 사분면 -> r이 h 이상, c가 h 이상
    if r < h and c < h: # 1사분면
        return find_ans(n - 1, r, c)
    elif r < h and c >= h: # 2사분면
        return find_ans(n - 1, r, c - h) + h**2
    elif r >= h and c < h: # 3사분면
        return find_ans(n - 1, r - h, c) + 2*(h**2)
    else: # 4사분면
        return find_ans(n - 1, r - h, c - h) + 3*(h**2)

# 2**n * 2**n 인 2차원 배열을 z모양으로 탐색
# n == 1일 경우 0, 0 -> 0, 1 -> 1, 0 -> 1, 1 순으로 순회
# n > 1일 경우 배열을 2**(n-1) * 2**(n-1) 배열로 4등분한 후 재귀 순회
# n, r, c가 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력

n, r, c = map(int, input().split())
print(find_ans(n, r, c))