# 문자열 입력받고 가장 많이 등장하는 알파벳과 개수 출력
arr = ['A', 'S', 'A', 'D', 'A', 'D', 'A', 'S']
arr_dict = {}
for i in arr:
    try:
        arr_dict[i] += 1
    except:
        arr_dict[i] = 1

max = 0
ans = ''
for i in arr_dict:
    if arr_dict[i] > max:
        max = arr_dict[i]
        ans = i

print(ans, max)