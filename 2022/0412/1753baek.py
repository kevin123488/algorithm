import sys
sys.stdin = open('1753.txt')

V, E = map(int, input().split())
s = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]