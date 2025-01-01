# 퀵정렬 -> 피봇을 활용하여 값을 비교해가며 정렬
# logN의 시간복잡도를 가짐

def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    before_pivot = []
    after_pivot = []
    cnt = 0
    for i in list:
        if i == pivot:
            cnt += 1
        elif i < pivot:
            before_pivot.append(i)
        elif i > pivot:
            after_pivot.append(i)

    return quick_sort(before_pivot) + [pivot * cnt] + quick_sort(after_pivot)

list = [10, 4, 23, 8, 22, 98, 64, 124, 77, 38, 99]
print(quick_sort(list))