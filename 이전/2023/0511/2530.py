import sys
sys.stdin = open('input2530.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())

s = d%60
m = d//60
h = m//60
m -= h*60

c += s
b += m
a += h

if c >= 60:
    c = c%60
    b += 1

if b >= 60:
    b = b%60
    a += 1

if a >= 24:
    a = a%24

print(a, b, c)