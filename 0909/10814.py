import sys
sys.stdin = open('10814.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    n = int(arr[len(arr)//2][0]) # pivot 값을 첫 값의 나이로 잡아주자

    s, m, b = [], [], []
    for i in arr:
        if int(i[0]) < n:
            s.append(i)
        elif int(i[0]) == n:
            m.append(i)
        else:
            b.append(i)
    return quick_sort(s) + m + quick_sort(b)

N = int(input())
# 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순으로 정렬하시오

arr = []
for i in range(N):
    age, name = input().split()
    arr.append([int(age), name])

for i in quick_sort(arr):
    print(i[0], end=' ')
    print(i[1])