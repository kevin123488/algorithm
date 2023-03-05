import sys
sys.stdin = open('15829input.txt')

L = int(input())
alpha_dict = {}
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(1, 27):
    alpha_dict[alpha_list[i-1]] = i

alpha = list(input())
ans = 0
for i in range(len(alpha)):
    ans += (alpha_dict[alpha[i]] * 31**i)

if ans > 1234567891:
    print(ans%1234567891)
else:
    print(ans)