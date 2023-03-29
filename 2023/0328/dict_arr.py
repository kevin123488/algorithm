nation_dict = {'KOREA': 3, 'CCC': 3, 'BBB': 9, 'AAA': 3}


sort_arr = []
for i in nation_dict:
    sort_arr.append([i, nation_dict[i]])
    # [[한국, 3], [c, 3], [b, 9], [a, 3]]

a = 1
while a < len(sort_arr): # sort_arr 길이 4 -> 1, 2, 3 까지
    for i in range(1, len(sort_arr) - a + 1): # 1, 2, 3
        if sort_arr[i][1] > sort_arr[i - 1][1]:
            sort_arr[i], sort_arr[i - 1] = sort_arr[i - 1], sort_arr[i]
    a += 1
print(sort_arr)

# a, b, c, d, e
#