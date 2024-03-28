def return_month(terms, alpha): # 약관에 따라 몇개월의 유효기간이 유지되는지 return
    for i in terms:
        alphabet = i[0]
        month = i[2:]
        if alphabet == alpha:
            return int(month)
        
def check_expire(start_date, expire_month, today): # 시작일, 유효기간, 오늘 날짜를 넣어주면 파기대상인지 아닌지 return
    year = int(start_date[0:4])
    month = int(start_date[5:7])
    date = int(start_date[8:10])
    
    next_month = month + expire_month
    next_year = year + next_month // 12
    next_month = next_month % 12
    next_date = date - 1
    if next_date == 0:
        next_date = 28
        next_month -= 1
    
    if next_month == 0:
        next_month = 12
        next_year -= 1
    
    today_year = int(today[0:4])
    today_month = int(today[5:7])
    today_date = int(today[8:10])
    
    if today_year > next_year:
        return 'expire'
    elif today_year == next_year:
        if today_month > next_month:
            return 'expire'
        elif today_month == next_month:
            if today_date <= next_date:
                return 'ok'
            else:
                return 'expire'
        else:
            return 'ok'
    else:
        return 'ok'
    
            
        
def solution(today, terms, privacies):
    # 입력값 예시
    # today: "2022.05.19"
    # terms: ["A 6", "B 12", "C 3"]
    # privacies: ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

    answer = []
    # 모든 달은 28일까지 있음
    for i in range(len(privacies)):
        start_date = privacies[i][0:10]
        yack_gwan = privacies[i][11]
        expire_YN = check_expire(start_date, return_month(terms, yack_gwan), today)
        
        if expire_YN == 'expire':
            answer.append(i + 1)
        
    return answer