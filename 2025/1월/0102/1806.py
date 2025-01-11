import sys
sys.stdin = open('input_1806.txt')

# 문제
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
# 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다.
# 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.
# 출력
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

n, s = map(int, input().split())
num_list = list(map(int, input().split())) # 길이 n
# 연속된 수들의 부분합 중 그 합이 S 이상이 되는 최소 길이
# 브루트 포스의 경우 -> 수열의 첫번째 칸부터 누적하여 값을 더함
# s의 값을 넘어서는 순간 수열의 길이를 기록
# 그 다음 값을 더하고 가장 앞의 값을 뺌
# 여전히 s 이상일 경우 가장 앞의 값을 하나 더 뺌

left, right = 0, 0
min_answer = n + 10
now_sum = 0
flag = 0

while True:
    if now_sum >= s:
        min_answer = min(min_answer, right - left)
        left += 1
        now_sum -= num_list[left - 1]
    
    elif right == n:
        break

    else:
        now_sum += num_list[right]
        right += 1
    
if min_answer == n + 10:
    print(0)
else:
    print(min_answer)