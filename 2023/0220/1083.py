import sys
sys.stdin = open('1083input.txt')

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# 소트할 때, 연속된 두개의 숫자만 교환 가능
# 최대 S회 교환 가능
# 정렬한 결과가 가장 뒷서는 결과를 출력
# 가장 뒷선다? -> 큰 값이 앞에 오도록

# 로직
# 앞으로 올 수 있는 값 중 가장 큰 값을 찾아야 한다.
# 1 2 3 4 5 일 경우 -> n번째 원소는 n-1회 정렬할 때 가장 앞으로 올 수 있다.
# 최대 S회 교환 가능하므로 S+1번째 값, 즉 arr[S] 값까지 후보군에 들어갈 수 있다.
# 그 후보군 안에서 가장 큰 값을 가장 앞으로 보내자
# S회에서 이동한 횟수를 빼주자. 편의상 K라고 하자. cnt 값은 += 1 해주자
# arr[cnt] 부터 arr[cnt+K]가 후보가 된다. 지금부턴 반복
# arr[cnt+K]의 범위는? 만약 cnt + K 값이 len(arr) 이상이라면 -> cnt + K 대신 len(arr)-1
cnt = 0
new_arr = [0, 0, 0]
while S > 0 or len(new_arr) <= 1:
    new_arr = arr[cnt:S+cnt+1] # 최댓값을 정해줘야 하는 후보군 리스트
    try:
        max_idx = new_arr.index(max(new_arr))
    except:
        break
    if max_idx == 0:
        pass
    else:
        S -= arr.index(max(new_arr))
        max_new_arr = arr.pop(arr.index(max(new_arr)))
        arr.insert(cnt, max_new_arr)
        # 5 3 1 2 4
        S += cnt
        if S <= 0:
            break
    cnt += 1

for i in arr:
    print(i, end=" ")