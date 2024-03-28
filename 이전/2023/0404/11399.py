import sys
sys.stdin = open('input11399.txt')
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split())) # i번째 사람이 돈을 뽑는데 걸리는 시간의 정보
# time = [3, 1, 4, 3, 2], 순서: 1 2 3 4 5
# 걸리는 시간의 총 합: 3 + (3 + 1) + (3 + 1 + 4) + (3 + 1 + 4 + 3) + (3 + 1 + 4 + 3 + 2) =
time.sort()
ans = 0
for i in range(len(time)): # 0 ~ 4
    ans += time[i] * (len(time) - i)

print(ans)