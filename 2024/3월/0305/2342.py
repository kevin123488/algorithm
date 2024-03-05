import sys
sys.stdin = open('2342.txt')

def by_left(f, nf):
    if f == 0:
        return 2
    elif f == 1 or f == 3:
        if nf == 2 or nf == 4:
            return 3
        else:
            return 4
    elif f == 2 or f == 4:
        if nf == 1 or nf == 3:
            return 3
        else:
            return 4


def by_right(f, nf):
    if f == 0:
        return 2
    elif f == 1 or f == 3:
        if nf == 2 or nf == 4:
            return 3
        else:
            return 4
    elif f == 2 or f == 4:
        if nf == 1 or nf == 3:
            return 3
        else:
            return 4

ddr = list(map(int, input().split())) # 0이 해당 배열의 끝
# 1: 위쪽, 2: 왼쪽, 3: 아랫쪽, 4: 오른쪽

# 왼발의 위치
dp_left = 0 # 위치. 0은 중앙점

# 오른발의 위치
dp_right = 0 # 위치. 0은 중앙점

# 시작할 때를 제외하면 두 발이 같은 위치에 있는 것을 허락하지 않음
# 중앙의 발이 다른 칸으로 이동할 때 -> 2만큼의 에너지 사용
# 인접한 칸으로 이동(위쪽에서 왼, 오), (아랫쪽에서 왼, 오), (왼쪽에서 위, 아래), (오른쪽에서 위, 아래) -> 3만큼의 에너지 사용
# 반대칸으로 이동(위쪽에서 아랫쪽), (아랫쪽에서 위쪽), (왼쪽에서 오른쪽), (오른쪽에서 왼쪽) -> 4만큼의 에너지 사용
# 같은 지점 한번 더 누름 -> 1만큼의 에너지 사용

ddr_dp = [0] * (len(ddr) + 1) # 처음 서있는 자리는 0 인덱스
for i in range(len(ddr)):
    if ddr[i] == 0:
        break
    # 왼발로 이동할 때
    # 오른발로 이동할 때
    # 단계별로 최솟값을 ddr_dp 리스트에 저장하자

    # 왼발로 이동
    if dp_left == ddr[i]:
        ddr_dp[i + 1] = ddr_dp[i] + 1
    # 오른발로 이동
    elif dp_right == ddr[i]:
        ddr_dp[i + 1] = ddr_dp[i] + 1

    else:
        # 왼발로 이동 할 때와 오른발로 이동 할 때를 비교하여 더 적은 값을 더해가자
        go_left = by_left(dp_left, ddr[i])
        go_right = by_right(dp_right, ddr[i])
        if go_left > go_right:
            ddr_dp[i + 1] = ddr_dp[i] + go_right
            dp_right = ddr[i]
        else:
            ddr_dp[i + 1] = ddr_dp[i] + go_left
            dp_left = ddr[i]

print(ddr_dp)
print(ddr_dp[len(ddr) - 1])