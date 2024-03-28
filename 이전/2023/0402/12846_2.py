import sys
sys.stdin = open('input12846.txt')
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        left = init(node * 2, start, mid)
        right = init(node * 2 + 1, mid + 1, end)
        if t[left] <= t[right]:
            tree[node] = left
        else:
            tree[node] = right
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_idx = query(node * 2, start, mid, left, right)
    right_idx = query(node * 2 + 1, mid + 1, end, left, right)
    if left_idx == -1:
        return right_idx
    elif right_idx == -1:
        return left_idx
    else:
        if t[left_idx] <= t[right_idx]:
            return left_idx
        else:
            return right_idx

def solve(start, end):
    if start > end:
        return 0
    idx = query(1, 0, n - 1, start, end)
    ans = t[idx] * (end - start + 1)
    ans_left = solve(start, idx - 1)
    ans_right = solve(idx + 1, end)
    return max(ans, ans_left, ans_right)

n = int(input())
t = list(map(int, input().split()))
tree = [0] * (4 * n)
init(1, 0, n - 1)
print(solve(0, n - 1))