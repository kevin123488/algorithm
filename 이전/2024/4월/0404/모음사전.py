from collections import deque

def make_word(tmp_list, word_list):
    q = deque()
    for i in word_list:
        q.append(i)
        
    while q:
        now_word = q.popleft()
        tmp_list.append(now_word)
        for i in word_list:
            if len(now_word) <= 4:
                q.append(now_word + i)

def solution(word):
    answer = 0
    tmp_list = []
    word_list = ['A', 'E', 'I', 'O', 'U']
    # word_list의 모음 5개를 가지고 (중복 허용) 단어를 쭉 만들자.
    # 단어의 길이는 최대 5개
    make_word(tmp_list, word_list)
    
    tmp_list.sort()
    
    for i in range(len(tmp_list)):
        if tmp_list[i] == word:
            answer = i + 1
            break
    
    return answer

word = 'AAAAA'
print(solution(word))