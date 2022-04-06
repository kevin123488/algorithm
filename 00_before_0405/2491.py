import sys
sys.stdin = open('2491.txt')

N = int(input()) # 수열의 길이
arr = list(map(int, input().split())) # 수열

# 연속해서 커지거나 작아지는 구간의 길이를 출력하면 되는 문제. ex) 4433221의 경우 7, 452211의 경우 5 이런 식으로 하면 됨
# 스택 써볼까?
ans_list = []
stack = []
# 우선 작아지는 경우일 때의 가장 긴 길이를 구해보자
arr_for_small = arr + [10000000000000000]
for i in range(len(arr)+1):
    if stack == []:
        stack.append(arr_for_small[i])
    else:
        if arr_for_small[i] <= stack[-1]:
            stack.append(arr_for_small[i])
        else:
            ans_list += [len(stack)]
            stack = []
            stack.append(arr_for_small[i])

# 그 다음은 커지는 경우
stack2 = []
arr_for_big = arr + [-1]
for z in range(len(arr)+1):
    if stack2 == []:
        stack2.append(arr_for_big[z])
    else:
        if arr_for_big[z] >= stack2[-1]:
            stack2.append(arr_for_big[z])
        else:
            ans_list += [len(stack2)]
            stack2 = []
            stack2.append(arr_for_big[z])

ans = max(ans_list)
print(ans)

# 문제 해결: 기본적인 스택의 운영방법으론 마지막 값이 쭉 이어지는 상태일 때 처리하기 힘들었다. 그래서 임의의 마지막 값을 추가해줬고,
# 마지막 값의 앞의 값(받아온 arr의 실제 마지막 값)을 기점으로 해당 stack의 쌓임이 끝남과 동시에 그 길이를 ans_list에
# 추가해주도록 하였다.