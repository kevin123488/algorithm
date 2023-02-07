import sys
sys.stdin = open('1978input.txt')

def find_sosu(num):
    for i in range(2, num): # 본인과 1은 제외하고 계산
        if not num%i: # 나눠 떨어지는 수가 있다 -> 소수가 아니다
            return False
    return True # 소수일 때 True 반환

N = input()
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if i == 1:
        pass
    elif find_sosu(i): # 소수 찾았으면 count에 +1
        count += 1

print(count)