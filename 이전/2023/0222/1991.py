import sys
sys.stdin = open('1991input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
tree = [0] * (2 * N + 1)
for i in range(len(arr)):
    pass
# A
# B   C
# D   E  F
#        G
# 위와 같은 형태로 트리가 형성됨
# 전위 순회: 중 왼 오
# 중위 순회: 왼 중 오
# 후위 순회: 왼 오 중

# 트리 작성 방법: 0번에 루트 노드
# 완전이진트리를 예로 들어보자.
# A
# B           C
# D     E     F     G
# H I   J K   L M   N O
# [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]
