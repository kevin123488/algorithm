import sys
sys.stdin = open('9012_input.txt')

# 괄호 문자열은 (, )으로 이루어진 문자열이다. 괄호의 모양이 바르게 된 문자열을 VPS라고 함
# 잘 열리고 닫혔다 -> VPS
# 입력받은 괄호 문자열의 VPS 유무를 판별하여 YES 혹은 NO를 나타내자

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    # arr의 요소들을 하나씩 조회하며 옳게 닫히면 YES를 출력, 중간에 엉키는 부분이 있으면
    # NO 출력
    # stack 사용
    st = [] # 선입선출의 특성을 이용
    flag = 0
    for i in arr:
        if i == '(':
            st.append(i) # 여는 괄호는 그냥 넣으면 됨. 잘못됨 여부는 닫는 괄호에서 판별
        elif i == ')':
            if st == []: # st가 비어있으면
                print('NO')
                flag = 1
                break
            elif st[-1] == '(': # 제일 최신의 괄호가 여는 괄호면
                st.pop(-1) # 마지막 요소 빼주고
            elif st[-1] == ')': # 제일 최신의 괄호가 닫는 괄호면
                print('NO')
                flag = 1
                break

    if flag:
        pass
    else:
        if st == []:
            print('YES')
        else:
            print('NO')