import sys
sys.stdin = open('baek_1018.txt')

# M*N 크기의 보드가 있음
# 이 보드를 잘라서 8*8짜리 보드로 만들 예정
# 체스판 -> 변을 공유하는 두 사각형의 색이 달라야 함
# 왼쪽 위가 흰색인 경우 / 왼쪽 위가 검정색인 경우로 구분됨
# 주어진 보드를 8*8크기의 보드로 자른 후 제대로 색칠되어있지 않은 부분을 다시 색칠하여 체스판을 만들려고 한다
# 가장 적은 횟수로 칠하는 경우의 칠하는 횟수를 구하여라

N, M = map(int, input().split())
print(N, M)