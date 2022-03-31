import sys
sys.stdin = open('2116.txt')

def maxdice(arr, a): # 주사위의 바닥면이 A일 경우, 즉 a가 0일 경우 해당 arr[i]의 최댓값을 max_ans에 넣어준 후 다음 단계로 넘어가는 함수
    global i
    global max_ans # 재귀 돌 때마다 0으로 초기화 된다. 이 부분을 해결하지 못하면 올바른 값을 구할 수 없을 것
    if i == len(arr)-1:
        return max_ans
    elif a == 0:
        k = max(arr[i][1], arr[i][2], arr[i][3], arr[i][4])
        b = arr[i][5]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)
    elif a == 1:
        k = max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
        b = arr[i][3]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)
    elif a == 2:
        k = max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
        b = arr[i][4]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)
    elif a == 3:
        k = max(arr[i][0], arr[i][2], arr[i][4], arr[i][5])
        b = arr[i][1]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)
    elif a == 4:
        k = max(arr[i][0], arr[i][1], arr[i][3], arr[i][5])
        b = arr[i][2]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)
    elif a == 5:
        k = max(arr[i][1], arr[i][2], arr[i][3], arr[i][4])
        b = arr[i][0]
        max_ans += k
        i += 1
        a = arr[i].index(b)
        maxdice(arr, a)

N = int(input()) # 주사위의 개수
arr = [list(map(int, input().split())) for _ in range(N)] # 주사위 각 면의 숫자 정보
arr.append([1, 2, 3, 4, 5, 6])
i = 0

max_list = []
for ii in range(6):
    max_ans = 0
    max_list.append(maxdice(arr, ii))
    i = 0

ans = max(max_list)
print(ans)
# 계속 밸류에러가 뜬다. 왜지? 큰맘먹고 재귀함수를 만들어 봤는데, 작동조차 안하다니... 어려워