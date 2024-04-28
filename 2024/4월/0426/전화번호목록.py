def solution(phone_book):
    answer = True
    # 어떤 번호가 다른 번호의 접두어 -> false
    # 접두어 아니다 -> true
    
    # 크게 고민할 것 없이 완전탐색 ㄱ
    
    # phone_book 리스트 순회하며 접두어 판별되면 break 후 false 리턴
    
    # 그 전에 phone_book 리스트를 길이순으로 정렬할 필요가 있음
    # 길이 짧은게 앞에 오게 하자
    # print(phone_book)
    
    phone_book.sort() # 가나다순으로 정렬(119, 1191이 있을 경우 둘이 연달아 나오게 됨)
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
                
                
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))