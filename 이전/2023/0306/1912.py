import sys
sys.stdin = open('1912input.txt')

n = int(input())
arr = list(map(int, input().split()))

# 연속된 몇 개의 수를 선택하여 구할 수 있는 합 중 가장 큰 값을 출력
# [10 -4 3 1 5 6 -35 12 21 -1]
ans = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        temp = sum(arr[i:j])
        if temp > ans:
            ans = temp

print(ans)