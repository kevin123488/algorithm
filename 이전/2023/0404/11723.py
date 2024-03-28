import sys
sys.stdin = open('input11723.txt')
input = sys.stdin.readline

m = int(input())
set_arr = []
for i in range(m):
    do = input().strip()
    if do[:3] == 'add':
        x = int(do[4:])
        set_arr.append(x)
        set_arr = list(set(set_arr))

    elif do[:3] == 'rem':
        x = int(do[7:])
        if x in set_arr:
            set_arr.pop(set_arr.index(x))

    elif do[:3] == 'che':
        x = int(do[6:])
        if x in set_arr:
            print(1)
        else:
            print(0)

    elif do[:3] == 'tog':
        x = int(do[7:])
        if x in set_arr:
            set_arr.pop(set_arr.index(x))
        else:
            set_arr.append(x)

    elif do[:3] == 'all':
        set_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    else:
        set_arr = []