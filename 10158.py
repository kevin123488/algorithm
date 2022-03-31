import sys
sys.stdin = open('10158.txt')

w, h = map(int, input().split()) # w: 가로, h: 세로
p, q = map(int, input().split()) # 개미의 첫 좌표. p: 가로, q: 세로
t = int(input()) # 개미가 이동하는 시간