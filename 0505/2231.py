import sys
sys.stdin = open('2231.txt')

def find_boon(a):
    # a의 분해합을 구하는 함수
    ans = a
    for i in str(a):
        ans += int(i)

    return ans

N = int(input())

# N의 분해합은? N이 240이라 쳤을 때, 240 + 2 + 4 = 246이 240의 분해합이 된다
# 이 경우, 240의 분해합이 246이므로 240을 246의 생성자라 한다
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구하는 프로그램을 작성하라

# 분해합이 N인 숫자중 가장 작은 수를 보이면 됨
for i in range(N+1):
    if find_boon(i) == N:
        print(i)
        break
else:
    print(0)