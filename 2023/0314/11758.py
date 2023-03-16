import sys
sys.stdin = open('11758input.txt')

# ccw 알고리즘
# 세 점의 방향성을 판단하는데 사용되는 알고리즘임
def ccw(x1, x2, x3, y1, y2, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

result = ccw(x1, x2, x3, y1, y2, y3)
if result == 0:
    print(0)
elif result > 0:
    print(1)
else:
    print(-1)