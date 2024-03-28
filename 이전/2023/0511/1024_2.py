import sys
sys.stdin = open('input1024.txt')
input = sys.stdin.readline

n, l = map(int, input().split())

for length in range(l, 101):
    # 길이가 length인 경우 가장 작은 시작점 s를 구한다.
    s = n // length - length // 2
    # s가 음이 아니고, 길이가 length일 때 합이 n이 되는지 확인한다.
    if s >= 0 and sum(range(s, s + length)) == n:
        # 길이가 100 이하인 경우 수열을 출력하고 프로그램을 종료한다.
        if length <= 100:
            print(" ".join(str(i) for i in range(s, s + length)))
            break
        # 길이가 100보다 큰 경우 -1을 출력하고 프로그램을 종료한다.
        else:
            print("-1")
            break
else:
    # 길이가 l부터 100까지 모든 경우를 확인해도 수열을 찾지 못한 경우 -1을 출력한다.
    print("-1")