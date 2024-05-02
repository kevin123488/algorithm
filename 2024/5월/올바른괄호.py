def solution(s):
    answer = True
    
    # 스택 활용하는 대표적인 문제
    if s[0] == ')' or s[-1] == '(':
        return False
    else:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                stack.pop()
        
        if stack == []:
            return True
        else:
            return False

s = '()'
print(solution(s))