import sys
sys.stdin = open('3020input.txt')

def find_idx_seuk(i):
    # 이분탐색을 활용, 부딪히기 시작하는 인덱스를 찾아내자.
    # 석순의 경우 i와 같거나 큰 값이 시작되는 부분을 찾으면 된다.
    start = 0
    end = len(seuk) - 1
    while end - start > 1:
        middle = (start + end) // 2
        if seuk[middle] >= i:
            end = middle
        elif seuk[middle] < i:
            start = middle

    if seuk[start] >= i:
        return start
    else:
        if seuk[end] >= i:
            return end
        else:
            return len(seuk)

def find_idx_yous(i):
    # 이분탐색을 활용, 부딪히기 시작하는 인덱스를 찾아내자.
    # 종유석의 경우 i와 종유석의 길이의 합이 H보다 커지는 값이 시작되는 부분을 찾으면 된다.
    start = 0
    end = len(yous) - 1
    while end - start > 1:
        middle = (start + end) // 2
        if i + yous[middle] > H:
            end = middle
        elif i + yous[middle] <= H:
            start = middle

    if i + yous[start] > H:
        return start
    else:
        if i + yous[end] > H:
            return end
        else:
            return len(yous)

N, H = map(int, input().split()) # N: 동굴의 길이, H: 동굴의 높이
huddle = []
for i in range(N):
    huddle.append(int(input()))

seuk = [] # 석순, 아래서 자람
yous = [] # 종유석, 위에서 자람
for i in range(len(huddle)):
    if i % 2: # i가 홀수 -> 짝수번째 요소 -> 종유석
        yous.append(huddle[i])
    else: # 석순
        seuk.append(huddle[i])

seuk.sort()
yous.sort()

# 종유석 목록과 석순 목록을 따로 분류해둠
# 비행 높이가 i -> 석순의 경우 i 이상일 때 부딪힘, 종유석의 경우 i + 종유석 길이가 H보다 커질 때 부딪힘
# 석순과 종유석의 부딪힘 포인트를 저장하자
len_seuk = len(seuk)
len_yous = len(yous)
seuk_point = len(seuk)
yous_point = len(yous)
ans = 1000000
ans_count = 0
for i in range(1, H+1):
    seuk_point = find_idx_seuk(i)
    yous_point = find_idx_yous(i)
    semi_ans = len_seuk - seuk_point + len_yous - yous_point
    if semi_ans < ans:
        ans = semi_ans
        ans_count = 1
    elif semi_ans == ans:
        ans_count += 1

print(ans, ans_count)