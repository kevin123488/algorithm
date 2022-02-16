import sys
sys.stdin = open('Baekjoon_1157_input.txt')
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

N = list(input().upper()) # 문자열의 형태로 입력값을 받는다
count_list = []
count_alpha_list = []

for i in N: # 받은 문자열을 순회 # aaaaabbbbbbb
    if i in count_alpha_list:
        pass
    else:
        count_alpha_list += [i] # ['a'], [5], # ['a', 'b'], [5, 7]
        count_list += [N.count(i)] # 문자열을 순회하며 순회중인 알파벳에 해당하는 count를 빈 리스트에 더해줌
                                   # 만약 기존에 더한적이 있는 알파벳이라면 중복을 방지하기 위해 더해주지 않음
    # count_list에서 제일 숫자 큰 애 인덱스 구하자
    # 그 인덱스와 같은 인덱스를 가지는 count_alpha_list의 값을 대문자로 반환하면 됨
    # 만약 최대치가 2개 이상이라면?
    # 물음표 반환. 이것은 count_list를 오름차순으로 정렬한 후 -1인덱스와 -2인덱스의 값이 같냐 다르냐로 판단 가능

max_idx = 0
max_ans = 0
for idx, j in enumerate(count_list):
    if j > max_ans:
        max_idx = idx
        max_ans = j
a = sorted(count_list)

if len(N) == 1:
    print(N[0])
elif a[-1] == a[-2]:
    print('?')
else:
    print(count_alpha_list[max_idx])