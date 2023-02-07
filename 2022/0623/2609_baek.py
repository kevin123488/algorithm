import sys
sys.stdin = open('2609_input.txt')

N, M = map(int, input().split())

# 첫 줄엔 최대공약수, 둘째 줄에는 최소공배수 출력
max_r = 1 # 최대공약수
min_r = 1 # 최소공배수
smaller = min(N, M)

for i in range(smaller, 0, -1):
    if N%i == 0 and M%i == 0:
        # 공약수를 찾아보자
        N /= i
        M /= i
        max_r *= i # 최대공약수와
        min_r *= i # 최소공배수를 계산해주자

min_r *= N
min_r *= M
print(int(max_r))
print(int(min_r))
# 위의 코드가 안되는 이유: 5가 공약수라 5로 양 숫자를 나눔 -> 5로 한번 더 나눌 수 있는데 안됨
# 이거 역순으로 가면서 큰 애들순으로 돌자