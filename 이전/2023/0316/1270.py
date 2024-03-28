import sys
sys.stdin = open('input1270.txt')

n = int(sys.stdin.readline())
for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    check = temp.pop(0)
    dict = {}
    for j in range(len(temp)):
        try:
            dict[temp[j]] += 1
        except:
            dict[temp[j]] = 1

    flag = 0
    for j in dict:
        if dict[j] > check/2:
            flag = 1
            print(j)
            break

    if flag == 0:
        print('SYJKGW')