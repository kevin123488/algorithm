import sys
sys.stdin = open('1181_input.txt')

# 길이가 짧은 순으로
# 길이가 같으면 사전순
# 중복제거

T = int(input())
arr = {}
for i in range(T):
    arr[input()] = 1

arr_list = []
for i in arr:
    arr_list.append(i)
print(arr_list)

arr_list.sort()
z = 0
while z <= len(arr_list):
    for i in range(len(arr_list) - 1):
        if len(arr_list[i]) > len(arr_list[i+1]):
            arr_list[i], arr_list[i+1] = arr_list[i+1], arr_list[i]
    z += 1

for i in arr_list:
    print(i)