import sys
sys.stdin = open('input11945.txt')

n, m = map(int, input().split())
arr = []
for i in range(n):
    li = input()
    temp = []
    for k in li:
        temp.append(int(k))
    arr.append(temp)

for i in arr:
    for k in list(reversed(i)):
        print(k, end='')
    print()