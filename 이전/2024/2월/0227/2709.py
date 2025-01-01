import sys
sys.stdin = open('2709.txt')

t = int(input())
for tc in range(t):
    r = int(input())

    # r이 주어졌을 때 마지막 R자리가 1과 2로만 이루어진 가장 작은 2**k를 구하는 프로그램을 작성

    # 규칙 찾기
    # k = 1 -> 2
    # k = 2 -> 4
    # k = 3 -> 8
    # k = 4 -> 16
    # k = 5 -> 32
    # k = 6 -> 64
    # k = 7 -> 128
    # k = 8 -> 256
    # k = 9 -> 512
    ans = 0
    for i in range(11687815589):
        ans *= 2
    
    print(0)