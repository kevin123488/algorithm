import sys
sys.stdin = open('2566.txt')

max_ans = -1
max_i = -1
max_j = -1
for i in range(9):
    list_input = list(map(int, input().split()))
    if max_ans > max(list_input):
        pass
    else:
        max_ans = max(list_input)
        max_i = i + 1
        max_j = list_input.index(max_ans) + 1

print(max_ans)
print(max_i, max_j)