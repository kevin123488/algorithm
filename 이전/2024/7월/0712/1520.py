import sys
sys.stdin = open('input_1520.txt')

m, n = map(int, input().split())

num_list = []
for i in range(m):
    num_list.append(list(map(int, input().split())))

print(m, n, num_list)