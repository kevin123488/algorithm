import sys
from itertools import combinations
sys.stdin = open('1759input.txt')

def make_ans(temp_list):
    ex_list = []
    for i in range(len(C_list)):
        if C_list[i] not in temp_list:
            ex_list.append(C_list[i])

    if L == 3:
        ans = ""
        temp_temp_list = temp_list[:]
        temp_temp_list.sort()
        for i in temp_temp_list:
            ans += i
        if ans not in the_real_ans_list:
            the_real_ans_list.append(ans)
    else:
        ex_list_comb = list(combinations(ex_list, L - 3))
        for i in ex_list_comb:
            temp_temp_list = temp_list[:]  # 얕은 복사
            for j in i:
                temp_temp_list.append(j)
                temp_temp_list.sort()
            ans = ""
            for k in temp_temp_list:
                ans += k
            if ans not in the_real_ans_list:
                the_real_ans_list.append(ans)

# 암호로 동작하는 암호 시스템
# 암호는 서로 다른 L개의 알파벳 소문자로 구성
# 최소 한개의 모음(a, e, i, o, u)과 최소 두개의 자음으로 구성
# 오름차순으로 배열. abc 가능, bca 불가능
# 암호로 사용했을 법한 문자의 종류는 C가지
# C개의 문자들이 모두 주어졌을 떄, 가능한 암호를 모두 구하는 프로그램을 작성

L, C = map(int, input().split())
C_list = list(input().split())
mou_em = []
ja_em = []
for i in C_list:
    if i in ['a', 'e', 'i', 'o', 'u']:
        mou_em.append(i)
    else:
        ja_em.append(i)

mou_em.sort()
ja_em.sort()
# mou_em에서 최소 1개, ja_em에서 최소 2개 뽑아서 만들어야 함
# 모음에서 1개를 빼고 자음에서 2개를 빼자. 모든 경우를 확인할 수 있게 해야한다. 그 뽑은 알파벳을 다른 리스트에 넣어두자.
# 위의 리스트에 들어간 요소를 제외하고 남은 알파벳 중 L-3개 만큼 뽐아본다.
# 리스트 + 뽑은 알파벳을 정렬하여 출력한다.

# 자음중 2개를 뽑는 경우를 조합을 이용해 생성해보자
ja_em_2 = list(combinations(ja_em, 2))
the_real_ans_list = []
for i in range(len(mou_em)): # 얘는 하나씩이니까 신경 쓸 필요 업다
    for j in range(len(ja_em_2)):
        temp_list = []
        temp_list.append(mou_em[i])
        temp_list.append(ja_em_2[j][0])
        temp_list.append(ja_em_2[j][1])
        make_ans(temp_list) # temp_list + temp_list에 포함되지 못한 알파벳들 중 L-3개 만큼 뽑는 경우를 조합하면 됨

the_real_ans_list.sort()
# print(the_real_ans_list)
for i in the_real_ans_list:
    print(i)