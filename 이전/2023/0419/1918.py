import sys
sys.stdin = open('input1918.txt')

arr = list(input())
ans = [] # A B C
stack = [] # * ( + )
op = ['+', '-', '*', '/', '(', ')']
# 로직 정리
# 1. 알파벳의 경우 정답 리스트에 바로 추가
# 2. 사칙연산의 경우 우선순위에 따라 로직 추가
# 2-1. +, -의 경우 스택에 넣자
# 2-2. *, /의 경우 스택에 넣고 자신보다 우선순위 높은거 나올때까지 스택의 값을 계속 뺴주자
# 2-3. (의 경우 스택에 넣고, )의 경우 스택에 넣지 말고 ( 나올때까지 스택에서 빼주자
# ans = [A, B, C, *, D, /, E, +, -]
# stack = [+, -,]
for i in range(len(arr)):
    if arr[i] in op:
        if arr[i] == '+' or arr[i] == '-':
            stack.append(arr[i])
        elif arr[i] == '*' or arr[i] == '/':
            stack.append(arr[i])
        else:
            if arr[i] == '(':
                stack.append(arr[i])
            else:
                while stack:
                    check_op = stack[-1]
                    if check_op == '(':
                        stack.pop()
                        break
                    else:
                        ans.append(stack.pop())
    # (C+D*E+G)
    else:
        ans.append(arr[i])
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
            while stack:
                if stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-':
                    ans.append(stack.pop())
                else:
                    break

for i in stack:
    ans.append(i)

for i in ans:
    print(i, end='')