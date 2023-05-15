import sys
sys.stdin = open('input1922.txt')
input = sys.stdin.readline

def is_cycle(temp):
    # 해당 간선이 사이클을 형성하면 1, 형성하지 않으면 0 return
    a, b = temp[1], temp[2]
    # 만약 linked에 [1, 2], [2, 3], [3, 4]가 들어가 있다고 치자. 입력받은 a, b가 1, 4일 경우 이 간선 조합은 사이클을 형성한다.

    # 이를 판별할 방법을 생각해보자
    if visited[a] == visited[b]:
        return 1
    else:
        if visited[a] > visited[b]:
            k = visited[a]
            for i in range(1, n + 1):
                if visited[i] == k:
                    visited[i] = visited[b]
        else:
            k = visited[b]
            for i in range(1, n + 1):
                if visited[i] == k:
                    visited[i] = visited[a]
        return 0

# 크루스칼 알고리즘 연습
n = int(input()) # 컴퓨터 개수
m = int(input()) # 간선 수
arr = []

for i in range(m):
    a, b, price = map(int, input().split())
    arr.append([price, a, b])

arr.sort()

# 크루스칼 알고리즘이란?
# 최소신장트리를 구하기 위한 알고리즘. 간선의 정보를 오름차순으로 정렬한 후, 가장 거리가 짧은 간선부터 더해감. 여기서 사이틀이 생기지 않도록 주의해야 함
ans = 0

# 부모 정보 초기화
visited = [0] * (n + 1)
for i in range(1, n + 1):
    visited[i] = i

cnt = 0
for i in range(m):
    if is_cycle(arr[i]) == 0:
        cnt += 1
        ans += arr[i][0]

    if cnt == n-1:
        break

print(ans)