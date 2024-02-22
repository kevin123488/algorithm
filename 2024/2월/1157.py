import sys
sys.stdin = open('1157.txt')
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

word = list(input())
dict = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
    'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 
    'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
    }
for i in word:
    dict[i.upper()] += 1

max_ans = [['abc', 0]]

for i in dict:
    if dict[i] > max_ans[-1][1]:
        max_ans = [[i, dict[i]]]
    elif dict[i] == max_ans[-1][1]:
        max_ans.append([i, dict[i]])

if len(max_ans) > 1:
    print('?')
else:
    print(max_ans[-1][0])