def solution(citations):
    answer = 0
    # 논문 n편중 h번 이상 인용된 논문이 h편 이상, 나머지가 h번 이하 인용
    # h의 최댓값이 해당 과학자의 H-index
    # citations -> 어떤 과학자의 논문 인용 횟수
    
    citations.sort(reverse = True)
    
    # i번 이상 인용된 논문의 수 구하기
    for i in range(1000, -1, -1): # 1000부터 0까지 역순으로 순회
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            return i
        
    return answer

cications = [3, 0, 6, 1, 5]
print(solution(cications))