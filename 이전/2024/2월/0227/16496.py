import sys
sys.stdin = open('16496.txt')

# 자릿수 비교 함수
def comparison_num(a, b):
    find_a = str(a)
    find_b = str(b)
    made_ans_1 = find_a + find_b
    made_ans_2 = find_b + find_a
    if made_ans_1 > made_ans_2:
        return a
    else:
        return b

n = int(input())
num_list = list(map(int, input().split()))
# 수끼리 비교해서 정렬하면 될 듯
# 결국 시간이 문제임. 우선 가장 직관적으로 생각나는 로직은
# 1. 각 자릿수끼리 비교하는 함수를 만들자.
# 고려할 부분: 9, 99, 9998 이렇게 있다고 치자. 9999998울 만드는게 가장 큰 수를 만드는 방법임. 자릿수를 자릿수 적은 수 기준으로 맞추고
# 한 자리씩 비교한 후 같다면 어떻게 처리해야 할까? 자릿수 적은 수를 먼저 써줘야 함
# 3, 34, 30이 있다고 치자. 34330으로 가는게 가장 큰 수를 만드는 방법임.

ans = ''
while num_list:
    for i in range(len(num_list)-1):
        upper_num = comparison_num(num_list[i], num_list[i + 1]) # 큰 수를 뒤로 보내고, 한번 순회 끝나면 가장 뒤에있는 수를 출력
        if upper_num == num_list[i]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    # print(num_list.pop(), end='')
    ans += str(num_list.pop())

print(int(ans))