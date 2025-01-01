def find_re(text):
    reporter = ''
    reportee = ''
    flag = 0
    for i in text:
        if i == ' ':
            flag = 1
        else:
            if flag == 0:
                reporter += i
            else:
                reportee += i
    
    return reporter, reportee
            

def solution(id_list, report, k):
    answer = []
    # 유저별로 한번에 한 명의 유저만 신고 가능
    # 서로 다른 유저를 계속해서 신고 가능, 한 유저 여러번도 가능하나 1회로 카운트
    # k번 이상 신고되면 게시판 이용 정지, 해당 유저 신고한 사람에게 메일
    # 유저가 신고한 모든 내용 취합 -> 마지막에 한꺼번에 정지시키고 메일 발송
    # 로직
    # 유저 아이디를 키값으로 갖는 딕셔너리 생성
    dict = {}
    for i in range(len(id_list)):
        dict[id_list[i]] = i
    
    report_result = [[0] * len(id_list) for _ in range(len(id_list))]
    # report_result[a][b] -> a가 b를 신고했는가 하지 않았는가 확인
    # id와 인덱스값(0 ~ len(id_list) - 1 사이의 값) 을 매핑시켜주는 작업 필요
    for i in report:
        reporter, reportee = find_re(i)
        report_result[dict[reporter]][dict[reportee]] = 1
    
    
    reported = [0] * (len(id_list)) # reported[i] = i가 신고당한 횟수
    # report_result[i] -> i가 신고한 대상
    
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if report_result[i][j] == 1:
                reported[j] += 1
    
    for i in range(len(id_list)):
        if reported[i] >= k: # 정지 대상
            reported[i] = 1
        else:
            reported[i] = 0
    
    # print(reported)
    # print(temp_list)
    # reported 값이 1인 대상을 신고한 id에 1 추가해주자
    answer = [0] * (len(id_list))
    for i in range(len(id_list)):
        if reported[i] == 1: # i 신고한 애들 값 추가
            for k in range(len(id_list)):
                if report_result[k][i] == 1:
                    answer[k] += 1
            
    return answer