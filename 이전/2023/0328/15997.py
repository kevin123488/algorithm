import sys
sys.stdin = open('input15997.txt')

def dfs(cnt, p):
    if cnt == 6:
        sort_arr = []
        for i in win_table:
            sort_arr.append([i, win_table[i]])

        a = 1
        while a < len(sort_arr): # sort_arr 길이 4
            for i in range(1, len(sort_arr) - a + 1):
                if sort_arr[i][1] > sort_arr[i - 1][1]:
                    sort_arr[i], sort_arr[i - 1] = sort_arr[i - 1], sort_arr[i]
            a += 1
        # win_table을 내림차순으로 바꿔주는 과정
        if sort_arr[0][1] == sort_arr[1][1] == sort_arr[2][1] == sort_arr[3][1]:
            ans_table[sort_arr[0][0]] += p / 2
            ans_table[sort_arr[1][0]] += p / 2
            ans_table[sort_arr[2][0]] += p / 2
            ans_table[sort_arr[3][0]] += p / 2
            return

        elif sort_arr[0][1] == sort_arr[1][1] == sort_arr[2][1]:
            ans_table[sort_arr[0][0]] += (p / 3 * 2)
            ans_table[sort_arr[1][0]] += (p / 3 * 2)
            ans_table[sort_arr[2][0]] += (p / 3 * 2)
            return

        elif sort_arr[1][1] == sort_arr[2][1] == sort_arr[3][1]:
            ans_table[sort_arr[0][0]] += p
            ans_table[sort_arr[1][0]] += p / 3
            ans_table[sort_arr[2][0]] += p / 3
            ans_table[sort_arr[3][0]] += p / 3
            return

        elif sort_arr[1][1] == sort_arr[2][1]:
            ans_table[sort_arr[0][0]] += p
            ans_table[sort_arr[1][0]] += p / 2
            ans_table[sort_arr[2][0]] += p / 2
            return

        else:
            ans_table[sort_arr[0][0]] += p
            ans_table[sort_arr[1][0]] += p
            return


    # 앞 국가가 이길 때
    win_table[fight[cnt][0]] += 3
    dfs(cnt + 1, p * float(fight[cnt][2]))
    win_table[fight[cnt][0]] -= 3

    # 비길 때
    win_table[fight[cnt][0]] += 1
    win_table[fight[cnt][1]] += 1
    dfs(cnt + 1, p * float(fight[cnt][3]))
    win_table[fight[cnt][0]] -= 1
    win_table[fight[cnt][1]] -= 1

    # 뒷 국가가 이길 때
    win_table[fight[cnt][1]] += 3
    dfs(cnt + 1, p * float(fight[cnt][4]))
    win_table[fight[cnt][1]] -= 3

nation = list(input().split())
win_table = {}
ans_table = {}
for i in nation:
    win_table[i] = 0
    ans_table[i] = 0

# A B W D L, A와 B가 경기했을 때 A가 이길 확률 -> W
fight = [list(input().split()) for _ in range(6)]
# 각 요소의 3, 4, 5번째 요소가 W D L
# 일어날 수 있는 모든 경우의 수를 체크하자
cnt = 0
dfs(cnt, 1)
for i in ans_table:
    print(ans_table[i])