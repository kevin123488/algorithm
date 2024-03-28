# 유진수란? 앞의 자릿수들의 곱과 뒤의 자릿수들의 곱이 같은 수를 의미한다
# 앞 그룹과 뒷 그룹은 나누기 나름
def gob(arr):
    ans = 1
    for i in arr:
        ans = ans * int(i)
    return ans

N = list(input())

# 1236이라는 수를 입력받으면 1-236, 12-36, 123-6 총 3가지로 케이스를 나누어 판별해야 한다
front_group = []
back_group = []
flag = 0
for i in range(1, len(N)): # 4자리의 숫자면 0부터 3까지, 문자열 슬라이싱을 이용하면
    front_group = N[:i]
    back_group = N[i:]
    # print(front_group)
    # print(back_group)
    if gob(front_group) == gob(back_group):
        print('YES')
        flag = 1
        break
if flag == 0:
    print('NO')