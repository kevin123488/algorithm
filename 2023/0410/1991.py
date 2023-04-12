import sys
sys.stdin = open('input1991.txt')
input = sys.stdin.readline

def preorder(node):
    if node in tree:
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node in tree:
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    if node in tree:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

n = int(input())
arr = [list(input().split()) for _ in range(n)]

tree = {} # 딕셔너리를 활용해 구현
for i in range(n):
    root, left, right = arr[i]
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')