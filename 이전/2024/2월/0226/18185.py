import sys
sys.stdin = open('18185.txt')

n = int(input())
ramen_list = list(map(int, input().split())) # 공장 1 ~ n까지 몇 개의 라면을 살 수 있는지 저장된 리스트

# 최소 비용으로 라면을 모두 구매하는 방법을 찾아야 함
# 하나의 공장에서 하나의 라면을 사면 3원
# 연속된 두개의 공장에서 라면을 하나씩 사면 5원
# 연속된 세개의 공장에서 라면을 하나씩 사면 7원
# 1 0 1의 경우 첫번쩨 공장에서 1개, 세번째 공장에서 1개 -> 6원이 최소
# 1 1 1 0 2의 경우 1, 2, 3번째 공장에서 하나씩 7원, 5번째 공장에서 3원짜리 2개로 6원

# 1 3 0 1 1
# 3개씩 끊어서 보도록 하자
# 1 1 1 3 -> 각각 사면 3 + 3 + 3 + 9 = 18, 2개씩 끊어 사면 
# 1 3 1 3
money = 0
all_sum = sum(ramen_list)
while all_sum > 0:
    for i in range(len(ramen_list) - 2):
        if ramen_list[i:i+3][0] > 0 and ramen_list[i:i+3][1] > 0 and ramen_list[i:i+3][2] > 0:
            ramen_list[i] -= 1
            ramen_list[i + 1] -= 1
            ramen_list[i + 2] -= 1
            all_sum -= 3
            money += 7
            if all_sum == 0:
                break
        
        elif ramen_list[i:i+3][1] == 0:
            if ramen_list[i:i+3][0] > 0:
                ramen_list[i] -= 1
                all_sum -= 1
                money += 3
                if all_sum == 0:
                    break
            
            if ramen_list[i:i+3][2] > 0:
                ramen_list[i + 2] -= 1
                all_sum -= 1
                money += 3
                if all_sum == 0:
                    break

        else:
            if ramen_list[i:i+3][0] > 0:
                ramen_list[i] -= 1
                ramen_list[i + 1] -= 1
                all_sum -= 2
                money += 5
                if all_sum == 0:
                    break
            
            if ramen_list[i:i+3][2] > 0:
                ramen_list[i + 1] -= 1
                ramen_list[i + 2] -= 1
                all_sum -= 2
                money += 5
                if all_sum == 0:
                    break

print(money)

# 6 7 5의 경우 3개들이로 5개 사고 2개들이 하나, 낱개로 1개 구매하는 방법과
# 2개들이 3개, 3개들이 4개를 사는 방법이 있다.
# 3 5 2 1 1 1의 경우 35 + 5 + 3 = 43
# 2 3 3 4의 경우 15 + 28 = 43