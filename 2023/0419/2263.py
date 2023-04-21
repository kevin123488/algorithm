import sys
sys.stdin = open('input2263.txt')
input = sys.stdin.readline

def build_tree(inorder, postorder, result):
    if len(inorder) < 1 and len(postorder) < 1:
        return

    root = postorder[-1]
    root_idx = inorder.index(root)

    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx + 1:]

    left_postorder = postorder[:root_idx]
    right_postorder = postorder[root_idx:len(postorder)-1]

    result.append(root)
    build_tree(left_inorder, left_postorder, result)
    build_tree(right_inorder, right_postorder, result)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

preorder = []
build_tree(inorder, postorder, preorder)
print(*preorder)
