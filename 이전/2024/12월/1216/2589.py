import sys
sys.stdin = open('input_2589.txt')

sero, garo = map(int, input().split())
map_list = [list(input()) for _ in range(sero)]

#
print(map_list)