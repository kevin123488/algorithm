import sys
sys.stdin = open('2559.txt')

N, K = map(int, input().split()) # N: 온도를 측정한 전체 날짜의 수, K: 합을 구하기 위한 연속적인 날짜의 수
t_list = list(map(int, input().split())) # t_list는 측정한 온도들의 리스트
# 연속적인 날짜 수만큼의 온도를 더한 값 중 최댓값을 출력하는 문제. ex) 4, 5, 6, 7, 8이라는 온도들의 나열과 K=3이라는 수를 받았을 경우,
# 답은 6+7+8 = 21

# 시간초과를 해결하기 위해서는 어떻게 해야 할까...
# 1. input 받을 때 readline어쩌구를 쓴다
# 2. pypy3으로 제출해본다
# 3. 코드를 새로 짜본다
max_sum = sum(t_list[0:K]) # idx 문제 X
su_m = sum(t_list[0:K])

for i in range(N-K): # 이렇게 잡아줘야됨
    su_m = su_m - t_list[i] + t_list[i+K]
    if max_sum < su_m:
        max_sum = su_m
print(max_sum)