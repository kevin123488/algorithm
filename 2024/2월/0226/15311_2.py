from sys import stdin
input = stdin.readline

n = int(input())

if n >= 1000:
    tmp_1 = n%1000
    tmp_2 = n // 1000
    if tmp_2 == 1000: # 백만일 경우 1000을 1000개 출력할수는 없으므로 따로처리
        print(1999)
        for _ in range(1000):
            print(1, end=' ')
        for _ in range(999):
            print(1000, end=' ')
        exit(0) # 처리후 코드 종료
    print(tmp_1+tmp_2) # 백만이하라면 1000으로 나눈 나머지와 1000으로 나눈 몫을 출력
    for _ in range(tmp_1):
        print(1, end=' ')
    for _ in range(tmp_2):
        print(1000, end=' ')
    print()
else:
    print(n) # 1000이하라면 그냥 1로 만들 수 있으므로 1 을 n개출력
    for _ in range(n):
        print(1, end=' ')
    print()