import sys
sys.stdin = open('6593input.txt')

#당신은 상범 빌딩에 갇히고 말았다. 여기서 탈출하는 가장 빠른 길은 무엇일까? 
# 상범 빌딩은 각 변의 길이가 1인 정육면체(단위 정육면체)로 이루어져있다. 
# 각 정육면체는 금으로 이루어져 있어 지나갈 수 없거나, 비어있어서 지나갈 수 있게 되어있다. 
# 당신은 각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동할 수 있다. 
# 즉, 대각선으로 이동하는 것은 불가능하다. 그리고 상범 빌딩의 바깥면도 모두 금으로 막혀있어 출구를 통해서만 탈출할 수 있다.
# 당신은 상범 빌딩을 탈출할 수 있을까? 만약 그렇다면 얼마나 걸릴까?

# tc는 3개의 정수(L, R, C)로 시작. L: 빌딩의 총 층, R: 한 층의 행, C: 한 층의 열
# 그 다음 각 줄이 C개의 문자로 이루어진 R개의 행이 L번 주어진다.
# 시작지점: S, 지나갈 수 없는 칸: #, 비어있는 칸: ., 출구: E, 각 층 사이에는 빈 줄이 있음, 입력의 끝은 0 0 0
# 각 빌딩에 대해 답을 출력. 
# 탈출 가능 -> Escaped in x minute(s).
# 탈출 불가능 -> Trapped!

building_list = [] # 빌딩들의 모든 정보를 담을 리스트
[
    {
        'LRC': [3, 2, 3],
        'floor': [
            [
                ['S', '.', '.', '.'],
                ['.', '.', '.', '.'],
                ['#', '.', '.', '#'],
                ['#', '.', '#', 'E']
            ], 
            [

            ], 
            [

            ]
        ] # 각 층의 정보를 담고있는 리스트 모음
    },
    {
        'LRC': [1, 2, 3],
        'floor': [
            []
        ]
    }
]
# 위의 형식으로 담을 예정
while True:
    L, R, C = map(int, input().split())
    print(L, R, C)
    dict = {}
    dict['LRC'] = [L, R, C]
    dict['floor'] = []
    for i in range(L): # L회만큼 빌딩의 층을 받아와야 한다
        one_floor = []
        for k in range(R):
            input = input()
            one_floor.append(input)
            print(one_floor)
        dict['floor'].append([one_floor])
    building_list.append(dict)
    print(building_list)