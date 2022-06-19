import sys
sys.stdin = open('5179.txt')

def make_tree(a): # 현재 조회중인 노드를 입력
    global cnt
    if a <= N:
        make_tree(2*a)
        tree[a] = cnt
        cnt += 1
        make_tree(2*a+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1부터 N까지의 숫자가 노드의 번호
    # 왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브트리의 루트
    # 위의 조건을 만족하는 트리를 짜자
    # 완전이진트리
    # 현재 노드의 인덱스를 n이라 치면
    # 왼쪽 서브트리 루트는 2n, 오서루는 2n+1이 될 것
    # 여기에 맞게 값을 넣어보자

    tree = [0] * (N+1)

    cnt = 1
    # 이제 트리를 순회하며 조건을 맞춰보자
    make_tree(1)
    print(tree)