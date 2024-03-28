import sys
sys.stdin = open('input11721.txt')

word = input()
temp = ''
for i in range(len(word)):
    temp += word[i]
    if len(temp) == 10:
        print(temp)
        temp = ''

print(temp)