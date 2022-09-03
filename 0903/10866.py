import sys
sys.stdin = open('10866.txt')

def push_front(x):
    global deque
    deque = [x] + deque

def push_back(x):
    global deque
    deque.append(x)

# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여덟 가지이다.
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

N = int(input()) # 주어지는 명령의 수
deque = []
commend = []
for i in range(N):
    commend.append(input())

for i in commend:
    if i == "front":
        try:
            print(deque[0])
        except:
            print(-1)
    elif i == "back":
        try:
            print(deque[-1])
        except:
            print(-1)
    elif i == "size":
        print(len(deque))
    elif i == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif i == "pop_front":
        try:
            print(deque.pop(0))
        except:
            print(-1)
    elif i == "pop_back":
        try:
            print(deque.pop(-1))
        except:
            print(-1)
    elif i[5] == "b":
        push_back(i[10:])
    else:
        push_front(i[11:])