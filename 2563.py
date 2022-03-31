import sys
sys.stdin = open('2563.txt')

whitepaper = [[0]*100 for _ in range(100)]
papers = int(input())
for paper in range(1, papers+1):
    paper_left, paper_under = map(int, input().split())
    # left 만큼 왼쪽 끝에서 떨어져서, under 만큼 아랫쪽 끝으로부터 떨어져서 색종이를 둬야 한다

    for i in range(100):
        for j in range(100):
            if 100-paper_under-10 <= i <= 100-paper_under-1 and paper_left <= j <= paper_left+9:
                whitepaper[i][j] = 1

cnt = 0
for k in range(100):
    for x in range(100):
        if whitepaper[k][x] == 1:
            cnt += 1

print(cnt)