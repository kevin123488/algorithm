# 백준 16637번 문제
# 괄호 추가하기
# 수식의 길이 N
# 구성: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, -, *
# 연산자들의 우선순위는 없음
# 괄호를 넣어 해당 수식의 값을 가장 크게 만들어라
import sys
sys.stdin = open('16637.txt')

N = int(input())
soosik = list(input())
# stack = []
#
# for i in range(N):
#     if stack == []:
#         stack.append(soosik[i])
#     elif soosik[i] in '+, -, *':
#         if soosik[i] == '+':
#             stack.append(int(stack[-1]) + int(soosik[i+1]))
#         elif soosik[i] == '-':
#             stack.append(int(stack[-1]) - int(soosik[i+1]))
#         else:
#             stack.append(int(stack[-1]) * int(soosik[i+1]))

# print(stack[-1])
# 이 문제는 브루트포스로 풀어야 한다. 모든 괄호의 경우의 수를 구한 후 해당하는 결과값을 비교하여 큰 값을 도출해야 한다.
# 어떻게 할 것인가? 해야 할 것은 1. 괄호의 위치 정하기 // 2. 정한 괄호의 위치에 맞는 계산로직 짜기 정도로 구분할 수 있다
