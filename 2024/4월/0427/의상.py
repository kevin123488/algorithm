def solution(clothes):
    answer = 0
    # print(clothes)
    	# [
    	# ['yellow_hat', 'headgear'], 
    	# ['blue_sunglasses', 'eyewear'], 
    	# ['green_turban', 'headgear']
    	# ]
        
    # 입을 수 있는 옷 조합 수 리턴
    # 딕셔너리 하나 만들자
    
    dict = {}
    for i in clothes:
        try:
            dict[i[1]].append(i[0])
        except:
            dict[i[1]] = [i[0]]
    
    # print(dict)
    # {
    #   'headgear': ['yellow_hat', 'green_turban'], 
    #   'eyewear': ['blue_sunglasses']
    # }
    
    # 딕셔너리 키값당 두개 이상의 요소를 선택할 수 없음
    # 선택된 의상의 수가 1개 이상이어야 함
    
    # 생각해보자. 현재 신경써야 하는 부분 -> 카테고리당 최대 1개의 의상을 선택할 수 있음.
    # 모든 카테고리에 대해 아무 옷도 선택하지 않는 경우는 없음
    # 어떤 카테고리에 옷이 2개 있다 치자. 여기서 나올 수 있는 가짓수는 1번 옷, 2번 옷, 아무 옷 선택 안함 총 3가지 가능
    # 모든 카테고리에 대해 카테고리의 의상 수 + 1 한 값을 곱해주고, 1을 빼주자(모두 선택 안하는 경우는 없기 때문)
    
    answer = 1
    for i in dict:
        answer *= (len(dict[i]) + 1)
    
    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))