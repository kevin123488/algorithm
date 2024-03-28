import sys
sys.stdin = open('input11403.txt')
input = sys.stdin.readline

n = int(input())
injeup = [list(map(int, input().split())) for _ in range(n)]
print(injeup)