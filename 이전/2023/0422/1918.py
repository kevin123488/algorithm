import sys
sys.stdin = open('input1918.txt')
input = sys.stdin.readline

arr = list(input().strip())
stack = []
op = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0,
    ')': 0
}

for i in range(len(arr)):
    if arr[i] in op:
        if len(stack) == 0:
            stack.append(arr[i])
        elif arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while True:
                op_ = stack.pop()
                if op_ == '(':
                    break
                print(op_, end='')
        else:
            while len(stack) > 0 and op[arr[i]] <= op[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(arr[i])
    else:
        print(arr[i], end='')

while len(stack) > 0:
    print(stack.pop(), end='')