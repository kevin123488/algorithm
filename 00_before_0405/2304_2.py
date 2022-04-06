import sys
sys.stdin = open('2304.txt')

N = int(input()) # 기둥의 개수
collist = [list(map(int, input().split())) for _ in range(N)] # 기둥의 정보가 담긴 리스트를 받아옴
collist.sort()

stack = []
ans = []
x_axis = []
for i in range(len(collist)):
    if stack == []:
        stack.append(0)
        ans.append(collist[i][1])
        x_axis.append(collist[i][0])
    elif collist[i][1] >= ans[-1]:
        stack.append(1)
        ans.append(collist[i][1])
        x_axis.append(collist[i][0])
    elif collist[i][1] < ans[-1]:
        stack.append(-1)