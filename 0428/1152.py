# arr = list(input().split())
# print(len(arr))

# 최고점수를 100으로 만들고 평균 만들기
# a = int(input())
# arr = list(map(int, input().split()))
#
# max_score = max(arr)
# joo_jak = []
# for i in arr:
#     joo_jak.append(i/max_score*100)
#
# ans = sum(joo_jak)/a
#
# print(ans)

# a = int(input())
#
# k = 1
# while k <= a:
#     for i in range(a-k):
#         print(' ', end='') # a-1개의 공백을 출력
#     ans = '*'*(k)
#     print(ans)
#     k += 1

# 자연수 3개(A, B, C) 가 주어질 때, A*B*C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성

# arr = []
# for i in range(3):
#     arr.append(int(input()))
#
# ans = 1
# for i in arr:
#     ans = ans*i
#
# real_ans = str(ans)
#
# dict = {
#     '0':0,
#     '1':0,
#     '2':0,
#     '3':0,
#     '4':0,
#     '5':0,
#     '6':0,
#     '7':0,
#     '8':0,
#     '9':0
# }
#
# for i in real_ans:
#     dict[i] += 1
#
# for i in dict:
#     print(dict[i])

# a = int(input())
# for i in range(a, 0, -1):
#     print(i)
# def read_it_reverse(a):
#     ans_str = ''
#     for i in range(len(a)-1, -1, -1):
#         ans_str += a[i]
#     return ans_str
#
# a, b = input().split()
#
# sang_a = int(read_it_reverse(a))
# sang_b = int(read_it_reverse(b))
#
# if sang_a > sang_b:
#     print(sang_a)
# else:
#     print(sang_b)


# ans_dict = {}
# for i in range(10):
#     a = int(input())
#     namerge = a%42
#     ans_dict[namerge] = 'hi'
#
# print(len(ans_dict))