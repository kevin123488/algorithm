import sys
sys.stdin = open('2467.txt')

n = int(input())
liquid_list = list(map(int, input().split())) # 용액의 특성을 숫자로 입력한 것
# 산성용액: 양의 정수
# 알칼리성 용액: 음의 정수
# 같은 양의 두 용액을 혼합한 용액의 특성값 -> 혼합에 사용한 각 용액의 특성값의 합으로 정의
# 같은 양의 두 용액을 합성하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.
# liquid_list에 있는 용액 중 두개를 골라 합하여 0에 가장 가까운 용액을 만들자.

# 투포인터 사용

left_idx = 0
right_idx = n - 1
min_ans = abs(liquid_list[left_idx] + liquid_list[right_idx])

ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:
    roop_ans = liquid_list[left_idx] + liquid_list[right_idx]

    if abs(roop_ans) < min_ans:
        min_ans = abs(roop_ans)
        ans_left = left_idx
        ans_right = right_idx

    # 만약 두 용액의 합이 음수라면? -> 음수에 해당할 가능성이 높은 left_idx 값을 하나 올려주자
    if roop_ans < 0:
        left_idx += 1
    elif roop_ans == 0:
        break
    else:
        right_idx -= 1

print(liquid_list[ans_left], liquid_list[ans_right])