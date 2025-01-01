import sys
sys.stdin = open('11286.txt')

# 절댓값 힙
# 배열에 정수 x(0이 아닌)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 다장 작은 값이 여러개일 때는 가장 작은 수를 출력한 후 그 값을 배열에서 제거한다.

# 힙큐 구현
def heap_que(heap_list, heap_num):
    heap_list.append(heap_num) # 끝부분에 원소 추가
    for i in range(len(heap_list) - 1, - 1, - 1):
        if abs(heap_list[i]) < abs(heap_list[i // 2]):
            heap_list[i], heap_list[i // 2] = heap_list[i // 2], heap_list[i]

    return heap_list


n = int(input())
cal_list = []
for i in range(n):
    num = int(input())
    if num != 0:
        cal_list = heap_que(cal_list, num)

    else:
        if len(cal_list) == 0:
            print(0)
        else:
            pick = abs(cal_list[0])
            flag = 0
            for j in range(len(cal_list)):
                if abs(cal_list[j]) == pick and cal_list[j] < 0:
                    print(cal_list.pop(cal_list.index(cal_list[j])))
                    flag = 1
                    break

            if flag == 0:
                print(cal_list.pop(0))

#                       -2
#             -1                   -1
#        0          0         -1         0
#     0    0     2    1     0    1     0    0
#    0 1  0