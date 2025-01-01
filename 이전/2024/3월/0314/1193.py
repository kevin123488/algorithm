import sys
sys.stdin = open('1193.txt')

x = int(input())

# 1/1, 1/2, 2/1, ...

sum = 2
cnt = 0
flag = 0
while True:
    if sum % 2: # 홀수
        for i in range(1, sum): # 분모가 큰 수부터
            boon_ja = i
            boon_mo = sum - i
            cnt += 1
            if cnt == x:
                flag = 1
                break
    
    else:
        for i in range(1, sum): # 분모가 작은 수부터
            boon_ja = sum - i
            boon_mo = i
            cnt += 1
            if cnt == x:
                flag = 1
                break
    
    if flag == 1:
        break
    sum += 1

ans = str(boon_ja) + '/' + str(boon_mo)
print(ans)