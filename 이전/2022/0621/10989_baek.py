import sys
sys.stdin = open('10989_input.txt')
N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
num_list.sort()
for i in num_list:
    print(i)