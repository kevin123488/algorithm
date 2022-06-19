import sys
sys.stdin = open('10250_input.txt')

A, B, V = map(int, input().split())

final = 0
cnt = 0

while True:
    final += A
    cnt += 1
    if final >= V:
        break
    else:
        final -= B

print(cnt)