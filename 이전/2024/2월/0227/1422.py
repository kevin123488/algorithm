import sys
sys.stdin = open('1422.txt')

def comparison_num(a, b):
    find_a = str(a)
    find_b = str(b)
    made_ans_1 = find_a + find_b
    made_ans_2 = find_b + find_a
    if made_ans_1 > made_ans_2:
        return a
    else:
        return b

k, n = map(int, input().split())
num_list = []
for i in range(k):
    num_list.append(int(input()))

find_which_num_insert = str(max(num_list))

ans = ''
flag = 0
while num_list:
    for i in range(len(num_list)-1):
        upper_num = comparison_num(num_list[i], num_list[i + 1]) # 큰 수를 뒤로 보내고, 한번 순회 끝나면 가장 뒤에있는 수를 출력
        if upper_num == num_list[i]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    # print(num_list.pop(), end='')
    temp = str(num_list.pop())
    ans += temp
    if temp == find_which_num_insert and flag == 0:
        flag = 1
        for j in range(n - k):
            ans += temp

print(int(ans))