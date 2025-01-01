import sys
sys.stdin = open('27172.txt')
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
max_card = max(card)
# print(n, card)

cards_with_idx = {card: idx for idx, card in enumerate(card)}
# print(cards_with_idx)

# 자기 카드로 상대방 수 나눴을 때 나누어 떨어지면 1점 get
# 상대방 수로 하여금 자신의 수가 나누어 떨어지면 1점 out
# 둘 다 아니면 0점

# 에라토스테네스의 채 알고리즘 활용

ans_list = [0] * n
for i in range(n):
    now_card = card[i]
    for j in range(now_card * 2, max_card + 1, now_card):
        if j in cards_with_idx:
            ans_idx = cards_with_idx[j]
            ans_list[i] += 1
            ans_list[ans_idx] -= 1
            # print(ans_list)

for i in ans_list:
    print(i, end=' ')

# print(ans_list)