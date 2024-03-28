import sys
sys.stdin = open('input5430.txt')
from collections import deque

T = int(sys.stdin.readline())
for tc in range(T):
    function = sys.stdin.readline().strip() # sys.stdin.readline으로 문자열을 받을 땐 strip()을 이용해 개행문자를 제거해줘야 한다.
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

    R_cnt = 0
    R_on = False
    flag = False
    for i in function:
        if i == 'R':
            if R_on:
                R_on = False
            else:
                R_on = True
            R_cnt += 1
        else:
            try:
                if R_on == False:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                flag = True
                print('error')
                break

    if flag:
        pass
    else:
        if len(arr) == 0:
            print('[]')
        else:
            print_ans = '['
            if R_cnt % 2:
                # 역으로 출력
                for i in range(len(arr)-1, -1, -1):
                    print_ans += str(arr[i])
                    print_ans += ','
            else:
                for i in range(len(arr)):
                    print_ans += str(arr[i])
                    print_ans += ','

            print_ans = print_ans[:-1]
            print_ans += ']'
            print(print_ans)
    # 뒤집는 횟수가 짝수다 -> 그대로, 홀수다 -> 반대로
    #