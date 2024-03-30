from collections import deque

def bfs(numbers, target, idx):
    q = deque()
    q.append([0, idx])
    cnt = 0
    
    while q:
        now_ans, now_idx = q.popleft()
        # [1, 2, 3]
        # target = 0
        if now_idx == len(numbers) - 1:
            if now_ans + numbers[now_idx] == target:
                cnt += 1
            if now_ans - numbers[now_idx] == target:
                cnt += 1
        
        if now_idx == len(numbers):
            return cnt
                
        
        next_ans_1 = now_ans + numbers[now_idx]
        next_ans_2 = now_ans - numbers[now_idx]
        q.append([next_ans_1, now_idx + 1])
        q.append([next_ans_2, now_idx + 1])
        

def solution(numbers, target):
    answer = 0
    # numbers 숫자들 적절이 더하거나 빼서 target 만드는 가짓수 리턴
    visited = [0] * len(numbers)
    # 각 숫자 앞에 +인지 -인지 구분 필요
    answer = bfs(numbers, target, 0)
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))