import sys
sys.stdin = open('input2113.txt')
input = sys.stdin.readline

k, a, d, n = map(int, input().split())
for i in range(k):
    mat = list(map(int, input().split()))
    print(mat)