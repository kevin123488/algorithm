def check_played(list):
    # print(list)
    list_2 = list[1:]
    # print(list_2)
    list_2.sort()
    # print(list_2)
    cnt_2 = 0
    while cnt_2 < len(list_2):
        for i in range(len(list_2) - 1 - cnt_2):
            # 적은거 뒤로 보내자
            if list_2[i][1] < list_2[i + 1][1]:
                list_2[i], list_2[i + 1] = list_2[i + 1], list_2[i]
        
        cnt_2 += 1
    
    if len(list_2) == 1:
        return [list_2[0][0]]
    else:
        return [list_2[0][0], list_2[1][0]]

def solution(genres, plays):
    answer = []
    # 노래 수록 기준
    # 속한 노래가 많이 재생된 장르 먼저 수록
    # 장르 내에서 많이 재생된 노래 먼저 수록
    # 장르 내에서 재생 횟수 같은 노레 중에선 고유 번호 낮은순 수록
    # 앨범에 들어갈 노래의 고유 번호를 순서대로 return
    
    # genres[i] -> 고유번호 i인 노래의 장르
    # plays[i] -> 고유번호 i인 노래가 재생된 횟수
    # 장르별로 딕셔너리를 만들어서 (인덱스, 재생횟수)를 리스트에 넣어주자
    
    dict = {}
    for i in range(len(genres)):
        try:
            dict[genres[i]].append([i, plays[i]])
            dict[genres[i]][0] += plays[i]
        except:
            dict[genres[i]] = [plays[i], [i, plays[i]]]
    
    # dict[genres[i]][0] -> 해당 장르의 플레이 총 수
    # print(dict)
    # 장르별 2곡씩 넣음
    
    # 딕셔너리 순회하며 총 플레이 수가 높은 장르순으로 정렬하자
    # 그 후 장르별로 재생 많이 된 인덱스 2개 골라 많이 들은 순으로 정렬
    # 만약 중복되었을 경우 인덱스 낮은거 포함시키자
    
    ans_list = []
    for i in dict:
        ans_list.append(dict[i])
        
    # 정렬 알고리즘을 활용해 총 플레이 수가 많은 순으로 정렬하자
    cnt = 0
    while cnt < len(ans_list):
        for i in range(len(ans_list) - 1 - cnt):
            # 재생 수 적은거 뒤로 보내자
            if ans_list[i][0] < ans_list[i + 1][0]:
                ans_list[i], ans_list[i + 1] = ans_list[i + 1], ans_list[i]
        
        cnt += 1
    
    # print(ans_list)
    # ans_list의 요소별로 재생수 많은 순 정렬 ㄱ
    for i in ans_list:
        semi_ans_list = check_played(i)
        for j in semi_ans_list:
            answer.append(j)
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))