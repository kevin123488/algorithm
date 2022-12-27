import sys
sys.stdin = open('16562input.txt')
sys.setrecursionlimit(100000)

def dfs(i):
    if friends_checklist[i] == 0:
        friendlump.append(friends[i])
        friends_checklist[i] = 1
    for k in range(len(friend_injeup[i])): # 친구 i에 대한 친구 관계를 확립하기 위함
        if friend_injeup[i][k] == 1 and friends_checklist[k] == 0: # k에 대한 친구를 발견했으면 + 아직 친구 설정이 안돼있으면
            friends_checklist[k] = 1 # 친구 체크하고
            friendlump.append(friends[k]) # 친구에 해당하는 친구비를 여기 넣자
            dfs(k) # 그 후 k에 대해 dfs 다시 돌자

# 학생 N명인 학교에 입학
# 모든 학생과 친구가 되고 싶다
# i에게 Ai만큼의 돈을 주면 한달간 친구가 될 수 있다. 준석이에겐 k원의 돈이 있다.
# 친구의 친구다 전법 사용
# 모든 친구에게 돈을 줄 필요는 없어졌다!
# 가장 적은 비용으로 모든 사람과 친구가 되는 방법은?

N, M, K = map(int, input().split()) # N: 학생 수, M: 친구관계 수, K: 소지금액
friends = [0] + list(map(int, input().split())) # N명의 학생들이 각각 원하는 친구비. 친구 번호와 인덱스를 맞춰주기 위해 0 추가
friends_relationship = []
for i in range(M):
    friends_relationship.append(list(map(int, input().split())))

# 친구의 친구는 친구다 -> dfs로 연결되어있는 친구들을 모두 체크하면 될 것 같다
# 학생 수 +1 만큼의 친구 체크 리스트를 만들어두자
friends_checklist = [0] * (N + 1) # 친구 번호와 인덱스를 일치시켜주기 위해

# 방향성이 없는 인접행렬을 만들어 줄 필요가 있어보인다
friend_injeup = [[0] * (N + 1) for _ in range(N + 1)]
for i in friends_relationship:
    friend_injeup[i[0]][i[1]] = 1
    friend_injeup[i[1]][i[0]] = 1

friends_lump = [] # 이곳에 친구 연결 단위를 리스트로 집어넣을 예정. 연결되어있는 친구들 덩어리를 뭉쳐서 정리해둔다고 생각. 넣는 값은 요구하는 친구비
# friends_lump를 순회하며 i의 min값을 ans에 더해가자

ans = 0
for i in range(N + 1):
    for j in range(N + 1):
        if friend_injeup[i][j] == 1: # 친구관계 발견했으면
            friendlump = []
            dfs(i) # 친구관계 시작점 얘로 잡고, 얘와 연결된 모든 친구를 체크하자
            friends_lump.append(friendlump)

for i in range(1, len(friends_checklist)):
    if friends_checklist[i] == 0: # 친구 안된 애가 있으면
        friends_lump.append([friends[i]])

for i in friends_lump:
    try:
        ans += min(i)
    except:
        pass

if ans > K:
    print("Oh no")

if ans <= K: # flag가 0이면 정답 출력
    print(ans)