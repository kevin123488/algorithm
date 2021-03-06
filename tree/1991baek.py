import sys
sys.stdin = open('1991.txt')

N = int(input()) # 이진트리의 노드의 개수
arr = [list(input().split()) for _ in range(N)] # 이진트리의 노드들의 자식 정보. 자식이 없는 경우, .으로 표시함

# arr의 요소가 만약 ['A', 'B', 'C']일 경우, A의 자식 노드 B, C라는 의미이고, ['A', 'B', '.']의 경우 A의 자식이 B 하나뿐이라는 의미이며
# ['A', '.', '.']의 경우 A의 자식노드가 존재하지 않는다는 의미이다.

al = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13,
      'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25,
      'Z':26}
# 입력받는 알파벳과 숫자를 연결시켜 두자

# 리스트를 만들고, 해당 노드들을 인덱스를 맞춰 넣어주도록 하자
for i in range(len(arr)):
