import math

def check_minute(list):
    # [['06:00', '18:12'], ['19:20']]
    all_time = 0
    for i in list:
        if len(i) == 2:
            all_time += (int(i[1][0:2]) * 60 + int(i[1][3:5]) - (int(i[0][0:2]) * 60 + int(i[0][3:5])))
        else:
            all_time += (23 * 60 + 59 - (int(i[0][0:2]) * 60 + int(i[0][3:5])))
    
    return all_time

def solution(fees, records):
    answer = []
    
    dict = {}
    money_dict = {}
    
    # 출차 이력 없으면 23시 59분 출차로 간주
    # 총 시간이 fees[0]분 이하 -> fees[1]원
    # fees[0]분 이상 -> fees[1] + |(시간 - fees[0]) / fees[2]| * fees[3]
    for i in range(len(records)):
        time = records[i][0:5]
        car_num = records[i][6:10]
        in_out = records[i][11:]
        try:
            if in_out[0] == 'I': # 들어올 때
                dict[car_num].append([time])
            else:
                dict[car_num][-1].append(time)
        except:
            dict[car_num] = [[time]]
    
    # print(dict)
    # {'0000': [['06:00', '18:12'], ['19:20']]}
    for i in dict:
        time_check = check_minute(dict[i])
        if time_check <= fees[0]:
            money_check = fees[1]
        else:
            money_check = fees[1] + math.ceil((time_check - fees[0]) / fees[2]) * fees[3]
        money_dict[i] = money_check
    
    sub_answer = []
    for i in money_dict:
        # sub_answer.append([i, money_dict[i]])
        sub_answer.append([i, money_dict[i]])
    
    
    cnt = 1
    while len(sub_answer) - cnt > 0:
        for i in range(len(sub_answer) - cnt):
            if sub_answer[i][0] > sub_answer[i + 1][0]:
                sub_answer[i], sub_answer[i + 1] = sub_answer[i + 1], sub_answer[i]
        
        cnt += 1
        
    for i in sub_answer:
        answer.append(i[1])
    
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))