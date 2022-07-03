import sys
sys.stdin = open('10828_input.txt')

N = int(input())
st = []
for tc in range(1, N+1):
    a = sys.stdin.readline().strip()
    if a[1] == 'u': # 만약 push 면
        st.append(int(a[5:]))
    elif a == 'top':
        try:
            print(st[-1])
        except:
            print(-1)
    elif a == 'pop':
        try:
            ans = st.pop(-1)
            print(ans)
        except:
            print(-1)
    elif a == 'size':
        print(len(st))
    elif a == 'empty':
        if st == []:
            print(1)
        else:
            print(0)