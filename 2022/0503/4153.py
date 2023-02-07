import sys
sys.stdin = open('4153.txt')

def pita(arr): # 배열을 인자로 받음
    a = max(arr)
    arr.pop(arr.index(a))
    if arr[0]**2 + arr[1]**2 == a**2:
        return 1
    else:
        return 0

arr = []
try:
    while True:
        arr.append(list(map(int, input().split())))
except:
    pass

arr.pop()
for i in arr:
    if pita(i):
        print('right')
    else:
        print('wrong')