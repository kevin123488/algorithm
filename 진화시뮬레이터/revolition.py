import sys
sys.stdin = open('rev.txt')
import random
# 진화 시뮬레이터

def rev(p: float) -> bool:
    return random.random() <= p

# 진화하고자 하는 선수 입력
player = input('진화하고자 하는 선수의 이름을 입력하세요: ')
print('')
player_0price = int(input('진화하고자 하는 선수의 0진 가격을 입력하세요(단위는 억 입니다. 정수로 입력해주세요.): '))
print('')
player_overall = int(input('진화하고자 하는 선수의 0진 오버롤을 입력하세요(125 이상): '))
print('')
player_goal = int(input('진화하고자 하는 목표 단계를 입력하세요: '))

# 진화 확률 정보 (풀게이지 기준)
# 0 -> 1: 100%
# 1 -> 2: 100%
# 2 -> 3: 81%
# 3 -> 4: 64%
# 4 -> 5: 50%
# 5 -> 6: 26%

rev_dict = {
    1: 1,
    2: 0.81,
    3: 0.64,
    4: 0.5,
    5: 0.26
}

price_dict = {
    125: 11,
    126: 15,
    127: 20,
    128: 30,
    129: 40,
    130: 60,
    131: 83,
    132: 100,
    133: 140,
    134: 170
}

print('모든 강화는 풀게이지 기준입니다. 0 -> 1의 경우 실금으로 붙인다 가정합니다.')
now_try = 1
paied_money = player_0price
try_cnt = 1

# 성공할 때 까지 진화 시작
while now_try != player_goal:
    paied_money += price_dict[player_overall] * 3
    if rev(rev_dict[now_try]):
        now_try += 1
    else:
        now_try -= 1
    try_cnt += 1

print('')
print('===== 결과 =====')
if try_cnt > 15:
    print(f'넌 진화하지 마라. {player_goal}진 하나 만드는데데 {try_cnt}번 시도하는놈은 처음 봤다. 니가 쓴 돈은 {paied_money}억이다. 차라리 사는게 나았을거다.')
else:
    print(f'{player_goal}진 성공, 시도 횟수: {try_cnt}, 지불된 금액: {paied_money}억')