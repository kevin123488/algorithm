import sys
sys.stdin = open('2467.txt')

n = int(input())
liquid_list = list(map(int, input().split())) # 용액의 특성을 숫자로 입력한 것
# 산성용액: 양의 정수
# 알칼리성 용액: 음의 정수
# 같은 양의 두 용액을 혼합한 용액의 특성값 -> 혼합에 사용한 각 용액의 특성값의 합으로 정의
# 같은 양의 두 용액을 합성하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
# liquid_list에 있는 용액 중 두개를 골라 합하여 0에 가장 가까운 용액을 만들자.

ans_list = [0, 0, 20000000000000] # 최솟값 나오면 a, b, a + b의 형태로 저장하자.
# a + b 값과 탐색 결과로 나온 두 용액의 합을 비교, 만일 결과값이 더 0과 가깝다면 변경

for i in range(len(liquid_list) - 1):
    for j in range(i + 1, len(liquid_list)):
        if abs(liquid_list[i] + liquid_list[j]) < abs(ans_list[2]):
            ans_list = [liquid_list[i], liquid_list[j], liquid_list[i] + liquid_list[j]]

print(ans_list[0], ans_list[1])
# 시간초과 해결 방안 -> 알고리즘 분류 참고하니 이분탐색과 투포인터 활용하라고 되어있음.
# 