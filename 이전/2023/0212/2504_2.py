import sys
sys.stdin = open('2504input.txt')

def well_gwal(arr):
    for i in range(len(arr)):
        if stack == []: # 저장되어 있는 괄호가 없으면
            stack.append(arr[i])

        elif stack[-1] == '(':
            if arr[i] == ')':
                stack.pop(-1)
            else:
                stack.append(arr[i])

        elif stack[-1] == ')':
            stack.append(arr[i])

        elif stack[-1] == '[':
            if arr[i] == ']':
                stack.pop(-1)
            else:
                stack.append(arr[i])

        elif stack[-1] == ']':
            stack.append(arr[i])

    if stack == []:
        return True
    else:
        return False

arr = list(input())
stack = []
index_score = {
    '(': 2,
    '[': 3
}
ans = 0
multi_ans = 0 # 조회중인 괄호의 값과 곱해줄 값을 의미
ans_list = []

if well_gwal(arr): # 괄호가 잘 닫힌다면
    for i in range(len(arr)):
        if stack == []:
            multi_ans = index_score[arr[i]] # 2
            ans = multi_ans
            stack.append(arr[i])
        else:
            if arr[i] == '(' or arr[i] == '[': # 스택이 비지 않은 상황에서, 여는 괄호가 들어오면
                multi_ans *= index_score[arr[i]]
                ans = multi_ans
                stack.append(arr[i])
            else:
                ans_list.append(ans)
                ans = 0
                if arr[i] == ')':
                    multi_ans //= index_score[stack[-1]]
                else:
                    multi_ans //= index_score[stack[-1]]
                stack.pop(-1)
    print(sum(ans_list))

else:
    print(0)