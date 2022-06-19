# print('|\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     print(a+b)
# X, N = map(int, input().split())
# arr = list(map(int, input().split()))
# for i in arr:
#     if i < N:
#         print(i)
# N = int(input())
# arr = list(map(int, input().split()))
# print(min(arr), end=' ')
# print(max(arr))
T = int(input())
for i in range(T):
    arr = list(input())

    ans = 0
    ans_list = []
    for i in arr:
        if i == 'X':
            for k in range(1, len(ans_list)+1):
                ans += k
            ans_list=[]
        else:
            ans_list.append(1)
    for k in range(1, len(ans_list) + 1):
        ans += k
    print(ans)