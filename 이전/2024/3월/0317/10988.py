import sys
sys.stdin = open('10988.txt')

word = input()
reverse_word = ''

for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]

if word == reverse_word:
    print(1)
else:
    print(0)