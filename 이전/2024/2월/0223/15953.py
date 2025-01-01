import sys
sys.stdin = open('15953.txt')

T = int(input())
for i in range(T):
    a, b = map(int, input().split()) # a는 2017 대회, b는 2018 대회 순위
    # 받을 수 있는 총 상금은?
    earn = 0
    # 2017 대회: 1 -> 500만, 2, 3 -> 300만, 4, 5, 6 -> 200만, 7, 8, 9, 10 -> 50만, 11, 12, 13, 14, 15 -> 30만, 16, 17, 18, 19, 20, 21 -> 10만
    if a == 1:
        earn += 5000000
    elif 2 <= a <= 3:
        earn += 3000000
    elif 4 <= a <= 6:
        earn += 2000000
    elif 7 <= a <= 10:
        earn += 500000
    elif 11 <= a <= 15:
        earn += 300000
    elif 16 <= a <= 21:
        earn += 100000

    if b == 1:
        earn += 5120000
    elif 2 <= b <= 3:
        earn += 2560000
    elif 4 <= b <= 7:
        earn += 1280000
    elif 8 <= b <= 15:
        earn += 640000
    elif 16 <= b <= 31:
        earn += 320000

    print(earn)