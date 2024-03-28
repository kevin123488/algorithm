import sys
sys.stdin = open('prac.txt')


def make_15(arr):
    # 받은 arr를 길이 15로 바꿔주는 리스트
    while True:
        if len(arr) < 15:
            arr.append('ABC')
        else:
            break

arr = [list(input()) for _ in range(5)] # 리스트에 담아주자
for i in arr:
    if len(i) < 15: # 해당 단어의 길이가 15보다 적다면?
        make_15(i) # 15로 만들어주자

# print(arr)
for k in range(15):
    for z in range(5):
        if arr[z][k] != 'ABC':
            print(arr[z][k], end='')