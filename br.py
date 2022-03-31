# baek 1000
# A, B =map(int, input().split())
# print(A+B)

# baek 1271
# n, m = map(int, input().split())
# print(n//m)
# print(n%m)

# baek 1550
# 16진수 입력받아 출력
# list = list(input())
# leng_th = len(list)
# ans = 0
# num = {
#     '0':0,
#     '1':1,
#     '2':2,
#     '3':3,
#     '4':4,
#     '5':5,
#     '6':6,
#     '7':7,
#     '8':8,
#     '9':9,
#     'A':10,
#     'B':11,
#     'C':12,
#     'D':13,
#     'E':14,
#     'F':15
# }
# for i in range(leng_th):
#     ans += num[list[-1-i]]*(16**i)
# print(ans)

# baek 2338
# A = int(input())
# B = int(input())
# print(A+B)
# print(A-B)
# print(A*B)

# baek 5337
# print('.  .   .')
# print('|  | _ | _. _ ._ _  _')
# print('|/\|(/.|(_.(_)[ | )(/.')

# baek 5338
# print('       _.-;;-._')
# print('\'-..-\'|   ||   |')
# print('\'-..-\'|_.-;;-._|')
# print('\'-..-\'|   ||   |')
# print('\'-..-\'|_.-\'\'-._|')

# baek 5522
# ans = 0
# for i in range(5):
#     ans += int(input())
# print(ans)

# baek 6749
# a = int(input())
# b = int(input())
# print(b-a+b)

# baek 8370
# a, b, c, d = map(int, input().split())
# print(a*b+c*d)

# baek 18096
# a = int(input())
# x ** 2 + 2x = a

# baek 1297
# D, H, W = map(int, input().split())
# a = D/((H**2+W**2)**(1/2))
# print(f'{int(H*a)} {int(W*a)}')

# baek 1330
# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a == b:
#     print('==')
# else:
#     print('<')

# baek 1712
# A만원의 고정비, B만원의 가변비
# A = 1000만, B = 70만이라고 하자. 10대 생산하면
# A + 10B = 1700만
# 노트북의 가격은 C만원. 총 판매 수입이 비용을 넘어서는 순간을 구하라
# 손익분기점 존재하지 않으면? -1 출력
# a, b, c = map(int, input().split())
# if b >= c: # 손익분기점이 없는 조건
#     print(-1)
# else: # a + nb < nc가 되는 n을 구해야 함
#     i = int(a/(c-b))
#     while True:
#         if a + i*b < i*c:
#             print(i)
#             break
#         else:
#             i += 1

# baek 2480
# 1~6까지의 눈을 가진 주사위 3개 던짐
# 같은 눈 3개 -> 10000+눈*1000의 상금
# 같은 눈 2개 -> 1000+눈*100의 상금
# 모두 다른 눈 -> 가장 큰 눈*100

# arr = list(map(int, input().split()))
# if arr[0] == arr[1] == arr[2]:
#     print(10000+arr[0]*1000)
# elif arr[0] == arr[1] or arr[0] == arr[2]:
#     print(1000+arr[0]*100)
# elif arr[1] == arr[2]:
#     print(1000+arr[1]*100)
# else:
#     print(max(arr)*100)

# baek 2525
# 시계문제
# time_list = list(map(int, input().split())) # 시, 분
# how_long = int(input()) # 요리가 얼마나 걸리는지
# k = time_list[1] + how_long # 분끼리 더한것
# a = k//60 # 분으로 받은 친구들은 합계 몇시간?
# b = k%60 # 시간으로 변환하고 남은 친구들
#
# # 시
# hour = (time_list[0] + a)%24
# # 분
# minute = b
# print(f'{hour} {minute}')

# baek 11382
# arr = list(map(int, input().split()))
# print(sum(arr))

# baek 13277
# a, b = map(int, input().split())
# print(a*b)

# baek 14652
# N, M, K = map(int, input().split()) # N*M 이차원리스트, 번호
# print(f'{K//M} {K%M}')

# baek 14928
# N = int(input())
# print(N%20000303)

# baek 10952
# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break
#     else:
#         print(A+B)

# baek 10171
# print('\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')