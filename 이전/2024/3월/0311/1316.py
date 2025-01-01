import sys
sys.stdin = open('1316.txt')

def find_group_word(a):
    # 각 문자가 연속해서 나오는 단어인지 체크하는 함수
    stack = [a[0]]
    for i in range(1, len(a)):
        if a[i] in stack and stack[-1] != a[i]:
            return False
        else:
            stack.append(a[i])
    
    return True


n = int(input())
word_list = [input() for _ in range(n)]

cnt = 0
for i in word_list:
    if find_group_word(i) == True:
        cnt += 1

print(cnt)