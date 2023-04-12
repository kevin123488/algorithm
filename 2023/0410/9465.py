import sys
sys.stdin = open('input9465.txt')
input = sys.stdin.readline

# 스티커 2n개 구매
# 2행 n열로 배치되어 있음
# 스티커 한 장을 떼면 그 스티커와 변을 공유하는 스티커는 모두 찢어져 사용할 수 없게됨
# 모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 메기고 점수의 합이 최대가 되게 스티커를 떼어내고자 한다.
#

t = int(input())
for tc in range(t):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    for i in range(1, n):
        if i == 1:
            l1[i] = l2[0] + l1[1]
            l2[i] = l1[0] + l2[1]
        else:
            l1[i] = max(l2[i-1], l2[i-2]) + l1[i]
            l2[i] = max(l1[i-1], l1[i-2]) + l2[i]

    print(max(l1[n-1], l2[n-1]))