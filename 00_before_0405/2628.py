import sys
sys.stdin = open('2628.txt')

garo, sero = map(int, input().split())
slice = int(input())
gase_line_num = [list(map(int, input().split())) for _ in range(slice)] # 가로면 0, 세로면 1.

garo_slice = [0] + [] # 가로로 자를 때
sero_slice = [0] + [] # 세로로 자를 때

for i in gase_line_num:
    if i[0] == 0: # 가로일 때
        garo_slice.append(i[1])
    else:
        sero_slice.append(i[1])

garo_slice.append(sero) # 가로로 자른다 -> 세로면에 영향
sero_slice.append(garo) # 세로로 자른다 -> 가로면에 영향
garo_slice.sort() # 0, 2, 3, 8
sero_slice.sort() # 0, 4, 10

stack = []
for z in range(1, len(garo_slice)):
    for x in range(1, len(sero_slice)):
        stack.append((garo_slice[z]-garo_slice[z-1])*(sero_slice[x]-sero_slice[x-1]))
print(max(stack))