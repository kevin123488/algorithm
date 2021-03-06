import sys
sys.stdin = open('10989_input.txt')

# 첫째 줄에 수의 개수 N이 주어짐. 범위는 1부터 10000000
# 둘째 줄부터 N개의 줄에 수가 주어짐. 10000보다 작거나 같은 자연수. 이 수들을 오름차순으로 정렬해서 보여줘야 함(1줄에 1개의 수가 나오도록)
# 리스트에 담아서 sort거는 방법은 100% 메모리 초과
# 또 무슨 방법이 있을까
N = int(input())
# 리스트에 넣긴 하는데, 방식을 새로이 생각해보자
num_arr = [0] * 10001 # 1부터 10000
for i in range(N):
    num_arr[int(sys.stdin.readline())] += 1
# [0, 1, 1, 0, 1, 2, 1, 0 ... ] 이런 식으로 리스트가 채워져 있을 것
# 리스트를 쭉 순회하면서 0이 아닌 값을 갖고있는 부분에 해당하는 인덱스를 해당 값만큼 출력하면 됨
# 그걸 이중포문으로 돌리면 시간초과가 남
# 어떻게 수정할까

for i in range(len(num_arr)):
    for k in range(num_arr[i]):
            print(i)