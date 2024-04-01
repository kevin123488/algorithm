from itertools import permutations
import math

def if_sosu(num_list):
    # 소수 -> 1과 자신 이외의 수로 나누어 떨어지지 않는 수
    num = ''
    for i in num_list:
        num += i
        
    num = int(num)
    
    if num <= 1:
        return 0, num # 소수가 아닐 경우 0 리턴
    
    flag = 0 # 나누어 떨어지는 케이스 나오면 1 추가
    for i in range(1, int(math.sqrt(num)) + 1):
        if num // i == num / i:
            flag += 1
    
    if flag == 1:
        return 1, num # 소수일 경우 1 리턴
    else:
        return 0, num
        

def solution(numbers):
    answer = 0
    # 문자열 주어짐
    # '123'이면 1, 2, 3 가지고 조합해서 만들 수 있는 소수 개수 리턴하면 됨
    # '17' -> 7, 17, 71 (1은 소수가 아님)
    
    # 숫자 조합 -> 순열을 활용해보자
    numbers_list = []
    for i in numbers:
        numbers_list.append(i)
        
    ans_dict = {}
    for i in range(1, len(numbers_list) + 1):
        ans_list = list(permutations(numbers_list, i))
        for j in ans_list:
            ans = if_sosu(j)
            if ans[0] == 1:
                ans_dict[ans[1]] = 1
                
    answer = len(ans_dict)
    
    # 7개의 문자열을 조합해 만들 수 있는 수
    # 1자리 -> 7개
    # 2자리 -> 42개
    # 3자리 -> 
    
    return answer

numbers = '1234567'
print(solution(numbers))