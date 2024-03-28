import sys
sys.stdin = open('1259.txt')

def find_pal(a):
    reversed_list = []
    a_list = []
    for i in a:
        a_list.append(i)

    for i in range(len(a)-1, -1, -1):
        reversed_list.append(a[i])

    if reversed_list == a_list:
        return 1
    else:
        return 0

arr = []
while True:
    try:
        arr.append(input())
    except:
        break

arr.pop()
for i in arr:
    if find_pal(i):
        print('yes')
    else:
        print('no')
