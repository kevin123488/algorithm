import time

n = 1000000

# 리스트 곱셈 사용
start = time.time()
visited1 = [0] * n
end = time.time()
print(f'리스트 곱셈 사용: {end - start}초')

# for문 사용
start = time.time()
visited2 = []
for i in range(n):
    visited2.append(0)
end = time.time()
print(f'for문 사용: {end - start}초')