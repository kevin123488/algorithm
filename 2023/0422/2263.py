import sys
sys.stdin = open('input2263.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=" ")

    left = node_num[root] - in_start
    right = in_end - node_num[root]

    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node_num = [0] * (n+1) # 찾고자 하는 root값이 몇 번째에 위치해있는지를 찾기 위해 만든 리스트
for i in range(n):
    node_num[inorder[i]] = i

preorder(0, n-1, 0, n-1)