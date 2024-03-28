import sys
sys.stdin = open('2504input.txt')

arr = list(input())
# ['(', '(', ')', '[', '[', ']', ']', ')', '(', '[', ']', ')']
# 2 * 2 + 2 * 3 * 3 + 2 * 3
# 2 * 2 + 2 * 3 * 3
# 괄호 열 때 스택 -1 값이 빈 값이 아니면 -> stack[-1]값과 arr[i]값을 곱해라. 괄호 닫을 때 더해라.
# stack이 비어있을 때 -> arr[i]에 해당하는 index_score 값을 ans에 더해줌
# 그 외 -> 여는 괄호가 나왔을 때 -> ans 값에 여는 괄호에 해당하는 index_score 값 곱해줌
# -> 닫는 괄호가 나왔을 때 -> 구해둔 ans 값을 during_ans에 넣고 ans 값 초기화
stack = []
ans = 0
during_ans = []
index_score = {
    '(': 2,
    '[': 3
}

for i in range(len(arr)):
    if stack == []: # 저장되어 있는 괄호가 없으면
        stack.append(arr[i])

    elif stack[-1] == '(':
        if arr[i] == ')':
            stack.pop(-1)
            during_ans.append(ans)
            try:
                ans = index_score[stack[-1]]
            except:
                ans = 0
        else:
            stack.append(arr[i])
            if arr[i] == '(' or arr[i] == '[':
                ans *= index_score[arr[i]]

    elif stack[-1] == ')':
        stack.append(arr[i])

    elif stack[-1] == '[':
        if arr[i] == ']':
            stack.pop(-1)
            during_ans.append(ans)
            try:
                ans = index_score[stack[-1]]
            except:
                ans = 0
        else:
            stack.append(arr[i])
            if arr[i] == '(' or arr[i] == '[':
                ans *= index_score[arr[i]]

    elif stack[-1] == ']':
        stack.append(arr[i])

if stack == []:
    print(during_ans)
else:
    print(0)