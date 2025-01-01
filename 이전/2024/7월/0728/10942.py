import sys
sys.stdin = open('10942.txt')

# 명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.
# 먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.
# 각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며,
# S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.
# 예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.
# S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
# S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
# S = 3, E = 3인 경우 1은 팰린드롬이다.
# S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
# 자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.
# 둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.
# 셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.
# 넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.

n = int(input())
black_board = list(map(int, input().split()))
m = int(input())
ques_list = [list(map(int, input().split())) for _ in range(m)]

# print(n, black_board, m, ques_list)
# 질문이 1 3 이면 칠판에 적힌 수 중 0번째 ~ 두번째 수 까지가 팰린드롬인지 아닌지를 판별하여 맞으면 1, 아니면 0 출력

dp = [[0] * n for _ in range(n)]
# dp[i][j] -> i번째 수에서 j번째 수 까지의 숫자가 팰린드롬인지 아닌치 판별하여 맞으면 1, 아니면 0 넣어주는 리스트

for i in range(n):
    dp[i][i] = 1
    if i > 0 and black_board[i - 1] == black_board[i]:
        dp[i - 1][i] = 1
        
# 부분 문자열별로 팰린드롬 판별
if n  > 2:
    for i in range(3, n + 1): # i는 문자열의 길이
        for j in range(n - i + 1): # j는 대상이 되는 문자열의 시작 인덱스 번호
            # 길이가 3이고 시작인덱스가 0 ~ 길이가 3이고 시작인덱스가 n - i
            k =  j + i - 1
            if black_board[j] == black_board[k] and dp[j + 1][k - 1] == 1:
                dp[j][k] = 1

for i in range(m):
    start_idx = ques_list[i][0] - 1
    fin_idx = ques_list[i][1] - 1
    print(dp[start_idx][fin_idx])