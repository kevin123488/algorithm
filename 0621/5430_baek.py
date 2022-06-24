import sys
sys.stdin = open('5430_input.txt')

N = int(input())
for tc in range(1, N+1):
    func_list = list(input())
    len_num = int(input())
    num_list = list(input())
    real_num_list = []
    for i in num_list:
        try:
            real_num_list.append(int(i))
        except:
            pass

    # R은 리스트 뒤집기, D는 가장 앞의 수 지우기
    try:
        for i in func_list:
            if i == 'R':
                real_num_list.reverse()
            else:
                real_num_list.pop(0)
        print(real_num_list)
    except:
        print('error')