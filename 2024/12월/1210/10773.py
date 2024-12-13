import sys
sys.stdin = open('input_10773.txt')

k = int(input())
num_list = []
for i in range(k):
    now_num = int(input())
    if now_num == 0:
        num_list.pop()
    else:
        num_list.append(now_num)

print(sum(num_list))