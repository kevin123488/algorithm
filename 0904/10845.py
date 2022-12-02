import sys
sys.stdin = open('10845.txt')

N = int(input())
commend = []
queue = []
for i in range(N):
    commend.append(input())

for i in commend:
    if i == 'pop':
        try:
            print(queue.pop(0))
        except:
            print(-1)
    elif i == 'size':
        print(len(queue))
    elif i == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif i == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif i == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
    else:
        queue.append(i[5:])