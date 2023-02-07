import sys
sys.stdin = open('10816.txt')

# 상근이는 숫자카드 N개를 가지고 있음
# 정수 M개가 주어졌을 때, 이 수 가 적혀있는 숫자 카드를 상근이가 몇 개 지니고 있는지 구해보자

N = int(input())
sang = list(map(int, input().split()))
M = int(input())
howmuch = list(map(int, input().split()))

# 당연하게도 시간초과 남
# 어떻게 해결?
# sang이 가지고 있는 것들을 딕셔너리로 만들어보자

sangdictionary = dict()
for i in sang:
    try:
        sangdictionary[i] += 1
    except:
        sangdictionary[i] = 1

for i in howmuch:
    try:
        print(sangdictionary[i], end=' ')
    except:
        print(0, end=' ')