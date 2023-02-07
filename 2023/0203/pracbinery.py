import sys
sys.stdin = open('pracbineryinput.txt')

def binery_search(i):
    start = 0
    end = len(arr) - 1
    while start + 1 < end:
        middle = (start + end) // 2
        if arr[middle] > i:
            end = middle
        elif arr[middle] < i:
            start = middle
        else:
            return middle

    if arr[start] >= i:
        return start
    else:
        if arr[end] >= i:
            return end
        else:
            return -1

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

arr.sort()
print(arr)
i = 20
ans = binery_search(i)
print(f"{i}의 높이로 날면")
if ans == -1:
    print("부딪히지 않습니다.")
else:
    print(arr[ans], "부터 부딪힙니다.")