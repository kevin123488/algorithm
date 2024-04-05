from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0])
    visited = [0] * len(words)
    
    while q:
        now_word, now_change_cnt = q.popleft()
        if now_word == target:
            return now_change_cnt
        
        for i in range(len(words)):
            # words[i]와 now_word가 한 글자만 달라야 함
            if visited[i] == 0:
                cnt = 0
                for j in range(len(now_word)):
                    if now_word[j] != words[i][j]:
                        cnt += 1

                if cnt == 1:
                    visited[i] = 1
                    q.append([words[i], now_change_cnt + 1])
        
    

def solution(begin, target, words):
    answer = 0
    # begin에서 target으로 단어 변환
    # 한번에 하나의 알파벳만 변경 가능
    # 변경 결과는 words에 속한 단어여야 함
    # 반환하는데 필요한 횟수 return
    # 반환 불가할 경우 0 return
    
    if target in words:
        answer = bfs(begin, target, words)
    
    return answer

begin = 'hii'
target = 'bye'
words = ['hie', 'hye', 'bye']

print(solution(begin, target, words))