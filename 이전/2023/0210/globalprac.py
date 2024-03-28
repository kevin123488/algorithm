def global1(ans):
    ans += 1
    return ans

ans = 0
ans = global1(ans)
print(ans)

def global2():
    global ans
    ans += 1

ans = 0
global2()
print(ans)