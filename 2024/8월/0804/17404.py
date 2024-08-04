import sys
sys.stdin = open('17404.txt')

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
# print(n, house)