import sys
sys.stdin = open('2304.txt')

N = int(input()) # 기둥의 개수
collist = [list(map(int, input().split())) for _ in range(N)] # 기둥의 정보가 담긴 리스트를 받아옴
collist.sort() # 좌표 순서대로 다시 정렬해줌

# 기둥의 길이를 모아둔 리스트를 하나 만들자
collength = []
for collen in range(len(collist)):
    collength += [collist[collen][1]]
ma_x = max(collength) # 가장 높은 기둥의 길이

stack = []
x_axis = []
# 왼쪽에서 조회하다 최댓값 만나면 종료 후 오른쪽에서 조회 시작하자
for i in range(len(collist)):
    if i == 0:
        stack.append(collist[i][1]) # 기둥의 첫값은 반드시 추가해줘야함
        x_axis += [collist[i][0]] # 나중에 넓이 계산할 때 쓸 예정
    else:
        if collist[i][1] == ma_x: # 만약 조회중인 요소가 최댓값이면?
            stack.append(ma_x)
            x_axis += [collist[i][0]] # 넓이 계산할 때 쓸 x좌푯값도 넣어주고
            break # break 해줌
        elif stack[-1] < collist[i][1]: # 최댓값은 아닌데 stack보다 크긴 하다면?
            stack.append(collist[i][1]) # 그 값 stack에 넣고
            x_axis += [collist[i][0]] # 넓이 계산할 때 쓸 x좌푯값도 넣어준 후 계속 돌자

# 여기까지 시작점~최댓값중 넓이 계산에 쓰이는 요소들을 stack과 x_axis에 넣어두었다
# 이제 끝에서 최댓값까지 도달하는 과정을 짜보자
stack2 = []
x_axis2 = []
# 위와 같은 방식으로 할 것
for ii in range(len(collist)-1, -1, -1): # 역순 조회 해야됨
    if ii == len(collist)-1:
        stack2.append(collist[ii][1])
        x_axis2 += [collist[ii][0]]
    else:
        if collist[ii][1] == ma_x:
            stack2.append(ma_x)
            x_axis2 += [collist[ii][0]]
            break
        elif collist[ii][1] > stack2[-1]:
            stack2.append(collist[ii][1])
            x_axis2 += [collist[ii][0]]

# print(stack, stack2, x_axis, x_axis2)
# 값들이 잘 받아와졌음을 확인했으니, 넓이를 계산해보자

ans = 0
for a in range(len(stack)-1):
    ans += stack[a]*(x_axis[a+1]-x_axis[a])

for b in range(len(stack2)-1):
    ans -= stack2[b]*(x_axis2[b+1]-x_axis2[b]) # 역순 조회이므로 x축의 길이(너비)가 음수로 책정됨. 그러므로 +=이 아닌 -=

# 최댓값과 최댓값 사이의 값을 더해줘야 함. 만약 최대높이가 2개라면, 위의 방식만으론 그 사이의 값을 더해줄 수 없음
ans += ma_x*(x_axis2[-1]-x_axis[-1]+1)

print(ans)