def find_ans(prices, now_idx):
    stack = []
    if now_idx == len(prices) - 1:
        return 0
    
    cnt = 0
    for i in range(now_idx + 1, len(prices)):
        if prices[now_idx] <= prices[i]: # 대상이 되는 주가가 오는 날들과 비교하여 값이 더 적거나 같을 때 -> 값이 떨어지지 않았다
            cnt += 1
        else:
            return cnt + 1 # 값이 떨어졌다면 떨어지는 날까지의 하루는 주가 유지로 인정이 되어야 하므로 + 1하여 return
    
    return cnt

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        answer.append(find_ans(prices, i))
        
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))