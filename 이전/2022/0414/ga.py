import random

def find(a, b):
    if a=='가위':
        if b=='가위':
            print('컴퓨터는 가위를 냈습니다. 비겼습니다. ')
        elif b=='바위':
            print('컴퓨터는 바위를 냈습니다. 졌습니다. ')
        elif b=='보':
            print('컴퓨터는 보를 냈습니다. 이겼습니다. ')
    elif a=='바위':
        if b=='가위':
            print('컴퓨터는 가위를 냈습니다. 이겼습니다. ')
        elif b=='바위':
            print('컴퓨터는 바위를 냈습니다. 비겼습니다. ')
        elif b=='보':
            print('컴퓨터는 보를 냈습니다. 졌습니다. ')
    elif a=='보':
        if b=='가위':
            print('컴퓨터는 가위를 냈습니다. 졌습니다. ')
        elif b=='바위':
            print('컴퓨터는 바위를 냈습니다. 이겼습니다. ')
        elif b=='보':
            print('컴퓨터는 보를 냈습니다. 비겼습니다. ')

print('가위, 바위, 보')
print('뭐 낼지 정해라')
a = input()
arr = ['가위', '바위', '보']
b = random.choice(arr)
find(a, b)