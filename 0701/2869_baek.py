import sys
sys.stdin = open('2869_input.txt')

A, B, V = map(int, sys.stdin.readline().split())
# 높이 V미터, 낮에 A미터 올라감, 밤에 B미터 올라감
# 정상에 올라간 후에는 미끄러지지 않음
# 정상에 도달하는데 걸리는 일수는?
# N = V // (A-B) + 1
# for i in range(N):
#     if A * i - B * (i - 1) >= V:
#         print(i)
#         break
# 시간초과
# 어떻게 해결하는게 좋을까?

N = V // (A-B) + 1
if A >= V:
    print(1)
else:
    for i in range(N, 0, -1):
        if A * i - B * (i - 1) < V:
            print(i+1)
            break