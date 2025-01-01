import sys
sys.stdin = open('10972.txt')
from itertools import combinations, permutations

def per_check(list_1):
    return_ans = []
    for i in list_1:
        return_ans.append(i)
    
    return return_ans

n = int(input())
suggested_comb = list(map(int, input().split()))

source_list = []
for i in range(1, 1 + n):
    source_list.append(i)

comb_list = list(permutations(source_list, n))

for i in range(len(comb_list)):
    if per_check(comb_list[i]) == per_check(suggested_comb):
        if i == len(comb_list) - 1:
            print(-1)
        else:
            for k in comb_list[i + 1]:
                print(k, end=' ')
            break