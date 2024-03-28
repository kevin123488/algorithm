import sys
sys.stdin = open('input2493.txt')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(N):
    if stack == []:
        stack.append([arr[i], i])
        print(i, end=" ")
    else:
        while len(stack) != 0:
            if arr[i] > stack[-1][0]:
                stack.pop()
            else:
                print(stack[-1][1] + 1, end=" ")
                break
        else:
            print(0, end=" ")
        stack.append([arr[i], i])