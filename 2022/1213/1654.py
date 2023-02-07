import sys
sys.stdin = open('1654input.txt')

k, n = map(int, input().split())
line_list = []

for i in range(k):
    line_list.append(int(input()))

start = 1
end = max(line_list)

while start <= end:
    mid = (start + end) // 2 # 1과 가장 큰 값의 합을 2로 나눈 몫에서 시작
    cnt = 0 # 카운트 0부터
    for i in line_list: # 끈이 들어있는 리스트를 순회하며
        cnt += i // mid # 로프 길이의 중간값을 이용, 해당 길이의 로프를 n개 만들 수 있는지 없는지 확인하자

    if cnt >= n: # 만들고자 하는 양보다 더 많이 생성했다?
        start = mid + 1
    else:
        end = mid - 1

print(end)