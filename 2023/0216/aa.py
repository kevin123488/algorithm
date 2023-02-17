arr = list(map(int, input().split()))
ans_list = []
ans_list.append(1-arr[0])
ans_list.append(1-arr[1])
ans_list.append(2-arr[2])
ans_list.append(2-arr[3])
ans_list.append(2-arr[4])
ans_list.append(8-arr[5])
for i in ans_list:
    print(i, end=" ")