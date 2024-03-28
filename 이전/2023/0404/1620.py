import sys
sys.stdin = open('input1620.txt')
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 도감에 수록된 포켓몬의 개수, m: 맞춰야 하는 문제의 개수
poket = list(input().strip() for _ in range(1, n + 1))
poket_dict = {}
for i in range(n):
    poket_dict[poket[i]] = i + 1
ques = list(input().strip() for _ in range(m)) # 문제가 알파벳이다? -> 포켓몬 번호 말하기, 번호디? 이름 말하기

for i in range(m):
    try:
        print(poket[int(ques[i]) - 1])
    except:
        print(poket_dict[ques[i]])