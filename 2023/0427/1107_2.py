import sys
sys.stdin = open('input1107.txt')
input = sys.stdin.readline

def bfs(num):
    # 여기 적용한 방식 말고 요소 하나씩 비교하는 방식도 문제 없음
    # 오히려 시간은 요소를 하나씩 비교하는 방식이 훨씬 빠름. 아마 사용 불가능한 요소가 나오자마자 False를 return할 수 있어서 그런 것 같음
    if set(str(num)) - non_fixed == set(str(num)):
        return True
    return False

n = int(input())
m = int(input())
non_fixed = set()
if m != 0:
    non_fixed = set(input().split())

if n == 100:
    print(0)
elif len(non_fixed) == 10:
    print(abs(n-100))
else:
    cnt = 0
    a = n
    b = n
    flag = 0
    ans_1 = 0
    ans_2 = 0
    while True:
        if bfs(a):
            ans_1 = min(cnt + len(str(a)), abs(n - 100))
            flag += 1
        if bfs(b):
            ans_2 = min(cnt + len(str(b)), abs(n - 100))
            flag += 1
        if flag == 0:
            pass
        elif flag == 1:
            print(max(ans_1, ans_2))
            break
        else:
            print(min(ans_1, ans_2))
            break
        cnt += 1
        a += 1
        if b >= 1:
            b -= 1