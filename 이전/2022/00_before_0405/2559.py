import sys
sys.stdin = open('2559.txt')

N, K = map(int, input().split()) # N: 온도를 측정한 전체 날짜의 수, K: 합을 구하기 위한 연속적인 날짜의 수
t_list = list(map(int, input().split())) # t_list는 측정한 온도들의 리스트
# 연속적인 날짜 수만큼의 온도를 더한 값 중 최댓값을 출력하는 문제. ex) 4, 5, 6, 7, 8이라는 온도들의 나열과 K=3이라는 수를 받았을 경우,
# 답은 6+7+8 = 21

sum_list = []
a = N-K+1
for i in range(a):
    sum_list += [sum(t_list[i:i+K])]

ans = max(sum_list)
print(ans)