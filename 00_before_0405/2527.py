import sys
sys.stdin = open('2527.txt')

for tc in range(1, 5):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x1>p2 or x2>p1 or q1<y2 or q2<y1: # 겹치지 않을 때
        print('d')
    elif (q1==y2 and p1==x2) or (p1==x2 and y1==q2) or (y1==q2 and x1==p2) or (q1==y2 and x1==p2): # 한 점만 만날 때
        print('c')
    elif x1==p2 or p1==x2 or q1==y2 or y1==q2:
        print('b')
    else:
        print('a')