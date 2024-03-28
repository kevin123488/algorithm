# 4
# 1 2 1 3 3 4 3 5
def pre(v): # 전위 순회
    if v:
        print(v) # visit
        pre(ch1[v]) # 왼쪽 가지 순회
        pre(ch2[v]) # 오른쪽 가지 순회

def inorder(v): # 중위 순회
    if v:
        inorder(ch1[v])
        print(v)
        inorder(ch2[v])

def post(v): # 후위 순회
    if v:
        post(ch1[v])
        post(ch2[v])
        print(v)

E = int(input()) # edge 수
arr = list(map(int, input().split()))
V = E + 1 # 정점의 수 == 1번부터 V번까지 정점이 있을 때 마지막 정점번호와 같음

# 부모를 인덱스로 자식번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없는 경우
        ch1[p] = c
    else:
        ch2[p] = c

print('--------')
print('pre 부분')
print('----1----')
pre(1)
print('----3----')
pre(3)
print('----5----')
pre(5)
print('--------')
print('inorder 부분')
print('----1----')
inorder(1)
print('----3----')
inorder(3)
print('----5----')
inorder(5)
print('--------')
print('post 부분')
print('----1----')
post(1)
print('----3----')
post(3)
print('----5----')
post(5)