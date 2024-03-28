import sys
sys.stdin = open('input1197.txt')
input = sys.stdin.readline

def is_cycle(temp):
    price, a, b = temp
    if node[a] == node[b]: # 부모가 같은 경우
        return True

    else:
        if node[a] > node[b]:
            x = node[a]
            for i in range(1, v + 1):
                if node[i] == x:
                    node[i] = node[b]

        elif node[a] < node[b]:
            x = node[b]
            for i in range(1, v + 1):
                if node[i] == x:
                    node[i] = node[a]

        return False

v, e = map(int, input().split())
# 최소 스패닝 트리 문제. 크루스칼 알고리즘을 사용하자
arr = []
for i in range(e):
    a, b, price = map(int, input().split())
    arr.append([price, a, b])

# 가중치 낮은 순으로 정렬
arr.sort()
node = [i for i in range(v + 1)]

ans = 0
cnt = 0
for i in range(e):
    if is_cycle(arr[i]) == False: # 사이클을 형성하지 않으면
        ans += arr[i][0]
        cnt += 1

    if cnt == v - 1:
        break

print(ans)