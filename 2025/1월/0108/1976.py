import sys
sys.stdin = open('input_1976.txt')

# 도시 n개, 임의의 두 도시 사이에 길이 있을수도 있고 없을수도 있음
# 동혁이의 여행 일정이 주어지면, 해당 일정이 수행 가능한지 판별하는 프로그램 ㄱ
# 
n = int(input())
m = int(input())

# 연결정보 저장
link_list = [0] * (n + 1)
for i in range(n):
    link_list.append(list(map(int, input().split())))

# 여행 계획 확인 - 여행 루트는 1 ~ n, 연결정보는 0 ~ n-1. 
journey = list(map(int, input().split()))