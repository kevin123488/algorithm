import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input1043.txt')
input = sys.stdin.readline

def check_party(arr, now_knows):
    check = [0, 0, 0, 0]
    for i in arr:
        if now_knows[i] == 1: # 진실을 아는 사람
            check[1] = 1
        elif now_knows[i] == 2: # 거짓말을 들은 사람
            check[2] = 1
        elif now_knows[i] == 3: # 진실을 들은 사람
            check[3] = 1
        else: # 진실을 모르며 진실도 거짓도 듣지 않은 사람
            check[0] = 1

    # 거짓말쟁이로 들통 -> return 0
    # 진실만 얘기 -> return 1
    # 거짓만 얘기 -> return 2
    # 진실과 거짓 모두 얘기 가능 -> return 3
    if check[1] == 1:
        if check[2] == 1:
            if check[3] == 1: # 진실을 아는 사람 있음, 거짓말 들은 사람 있음, 진실 들은 사람 있음
                return 0
            else: # 진실 아는 사람 있음, 거짓말 들은 사람 있음, 진실 들은 사람 없음
                return 0
        else:
            if check[3] == 1: # 진실 아는사람 있음, 거짓말 들은 사람 없음, 진실 들은 사람 있음
                return 1
            else:
                return 1

    else:
        if check[2] == 1:
            if check[3] == 1: # 진실 아는사람 없음, 거짓말 들은 사람 있음, 진실 들은 사람 있음
                return 0
            else: # 진실 아는사람 없음, 거짓말 들은 사람 있음, 진실 들은사람 없음
                return 2
        else:
            if check[3] == 1: # 진실 아는사람 없음, 거짓말 들은사람 없음, 진실 들은사람 있음
                return 1
            else: # 진실 아는사람 없음, 거짓말 들은사람 없음, 진실 들은사람 없음
                return 3

# 어떤 파티에서 진실을 듣고 어떤 파티에서는 거짓을 들었을 경우 또한 거짓말 발각의 원인이 될 수 있다.
def bfs(ans):
    q = deque()
    q.append([ans, now_people, 0])
    while q:
        now_ans, now_knows, now_party = q.popleft() # now_knows에는 현재 지민이의 진실을 알고 있는 사람들의 정보가 담겨있다.
        # 만약 진실을 알고 있다 -> 1 표시
        # 거짓말을 들었을 경우 2 표시, 진실을 들었을 경우 3 표시
        # 0에서 거짓말을 들었을 경우 2로, 탐색할 파티에 2인 상태가 있다면 진실은 말할 수 없다.
        # 0에서 진실을 들었을 경우 3으로, 탐색할 파티에 3인 상태가 있다면 거짓말은 할 수 없다.
        # 즉, 탐색중인 파티에서 진실을 알고 있는 사람이 없고, 이전에 진실을 들은 사람이 없다면 진실과 거짓을 말할 수 있다. (탐색중인 파티에 1과 3이 없을 경우)
        # 탐색중인 파티에서 진실을 알고 있는 사람이 없고, 이전에 진실을 들은 사람이 있다면 진실만을 말해야 한다.
        # 탐색중인 파티에서 진실을 알고 있는 사람이 있고, 이전에 거짓을 들은 사람이 있다면 해당 파티에선 반드시 거짓이 들통난다. 해당 탐색은 유망하지 않기에 포기해야 한다.
        # 탐색중인 파티에서 진실을 알고 있는 사람이 있고, 이전에 거짓을 들은 사람이 없다면 진실만을 말해야 한다.
        # ans = max(ans, now_ans)
        # print(ans, now_ans)
        if now_party == m:
            while q:
                ans = max(ans, q.popleft()[0])
            return ans
        check_result = check_party(party[now_party][1:], now_knows)

        if check_result == 1:
            # 진실만 얘기
            now_knows_copy = deepcopy(now_knows)
            for i in party[now_party][1:]:
                if now_knows[i] == 0:
                    now_knows_copy[i] = 3
            q.append([now_ans, now_knows_copy, now_party + 1])

        elif check_result == 2:
            # 거짓만 얘기
            now_knows_copy = deepcopy(now_knows)
            for i in party[now_party][1:]:
                if now_knows[i] == 0:
                    now_knows_copy[i] = 2
            q.append([now_ans + 1, now_knows_copy, now_party + 1])

        elif check_result == 3:
            # 진실과 거짓 모두 얘기 가능
            now_knows_copy = deepcopy(now_knows)
            for i in party[now_party][1:]:
                if now_knows[i] == 0:
                    now_knows_copy[i] = 3
            q.append([now_ans, now_knows_copy, now_party + 1])

            now_knows_copy2 = deepcopy(now_knows)
            for i in party[now_party][1:]:
                if now_knows[i] == 0:
                    now_knows_copy2[i] = 2
            q.append([now_ans + 1, now_knows_copy2, now_party + 1])

        else:
            # 거짓말쟁이로 들통
            pass

# 사람의 수 n이 주어진다
# 그 이야기의 진실을 아는 사람이 주어진다
# 파티에 오는 사람들의 번호가 주어진다
# 지민이는 모든 파티에 참가한다
# 지민이가 거짓말쟁이로 알려지지 않으면서 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하자

n, m = map(int, input().split())
real_man = list(map(int, input().split()))
# 리스트의 길이가 1이면 진실을 아는 사람은 없음,
# 2이상이면 첫번째 값이 진실을 아는 사람의 수, 두번째 값부터 진실을 아는 사람의 목록
party = [list(map(int, input().split())) for _ in range(m)]
# 각 파티마다 오는 사람의 수와 그 사람들의 번호가 주어짐. ex) 2 1 5 -> 해당 파티 참가자 2명, 1과 5번 손님

now_people = [0] * (n+1)

for i in range(1, len(real_man)):
    now_people[real_man[i]] = 1

ans = 0
print(bfs(ans))