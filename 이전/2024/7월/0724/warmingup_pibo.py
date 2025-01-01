import sys
sys.stdin = open('pibo.txt')

n = int(input())
pibo_list = [0] * (n + 1)

if n >= 0:
    pibo_list[0] = 0

if n > 0:
    pibo_list[1] = 1

    for i in range(2, n + 1):
        pibo_list[i] = pibo_list[i - 1] + pibo_list[i - 2]

print(pibo_list[n])