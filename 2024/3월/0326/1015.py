import sys
sys.stdin = open('1015.txt')
from copy import deepcopy

n = int(input())
list_a = list(map(int, input().split()))


# 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.
b = [0] * n

# 입력받는 값 순서 메기고
# 그 순서값을 정렬했을 때 수가 가장 적게 나오도록 하면 됨(같은 수의 경우 큰 수를 뒤로 보내는 형식)

p = [i for i in range(n)]

# list_a가 [3, 1, 2]로 있다고 치자.
# 여기서 리턴해야 할 값은 각 값의 순서에 해당하는 [2, 0, 1]
# list_a의 0번째 값인 3은 순서대로 정렬했을 때 2번 인덱스에 위치하므로 리턴할 값에는 2를 적어주는 것

sort_list_a = sorted(list_a)

# list_a를 순회하며 각 값이 sort_list_a의 몇번째 인덱스에 해당하는지를 출력하면 됨

ans_list = []
visited = [0] * n

for i in list_a:
    flag = 0
    for j in range(n):
        if i == sort_list_a[j] and visited[j] == 0 and flag == 0:
            ans_list.append(j)
            visited[j] = 1
            flag = 1

for i in ans_list:
    print(i, end=' ')