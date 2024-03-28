# 피보나치 수열
def fibo(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(1, 41): # 수열의 40번째까지 표시
    print(fibo(i))