import sys
sys.stdin = open('input5430.txt')
from collections import deque

def reverse(arr):
    return_ans = deque()
    for i in range(len(arr)-1, -1, -1):
        return_ans.append(arr[i])
    return return_ans

def find_ans(arr):
    for i in function:
        if i == 'R':
            # 순서 뒤집는 함수
            arr = reverse(arr)
        else:
            if len(arr) == 0:
                return 'error'
            else:
                arr.popleft()

    return_ans = []
    for i in arr:
        return_ans.append(i)
    return return_ans

T = int(sys.stdin.readline())
for tc in range(T):
    function = sys.stdin.readline().strip() # sys.stdin.readline으로 문자열을 받을 땐 strip()을 이용해 개행문자를 제거해줘야 한다.
    # print(function)
    n = int(sys.stdin.readline())
    arr = deque()
    arr_input = sys.stdin.readline().strip()
    case = ['[', ']', ',']
    temp = ''
    for i in arr_input:
        if i not in case:
            temp += i
        elif temp != '':
            arr.append(int(temp))
            temp = ''

    print(find_ans(arr))