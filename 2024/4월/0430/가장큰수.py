def solution(numbers):
    answer = ''
    # 이거 생각해내는게 조금 어려울 수 있음
    numbers2 = []
    for i in numbers:
        numbers2.append(str(i) * 3)
    
    numbers2.sort(reverse=True)
    
    for i in numbers2:
        if len(i) == 3:
            answer += i[0]
        elif len(i) == 6:
            answer += i[:2]
        elif len(i) == 9:
            answer += i[:3]
        else:
            answer += '1000'
    
    return str(int(answer)) # 00000 이런 수가 만들어질 때 0을 출력해야 함

numbers = [1, 2, 3, 4, 5]
print(solution(numbers))