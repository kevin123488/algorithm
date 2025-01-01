import sys
sys.stdin = open('input_2225.txt')

n, k = map(int, input().split())

# 0부터 n까지의 정수 중 k개를 더해 그 합이 n이 되는 경우의 수를 구하자
# 한개의 수를 여러번 쓸 수도 있음
# 20 2 일 경우 0 20 ~ 20 0 해서 총 21가지

