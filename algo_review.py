# 1. 버블정렬
# 1-1. 가장 큰 값을 뒤로 보내는 작업
arr = [4, 1, 6, 3, 4, 9, 3, 10, 2, 1, 3, 4, 2, 5, 1, 4]
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         arr[i], arr[i+1] = arr[i+1], arr[i]
# 가장 큰 값이 arr의 끝에 들어가게 됨

# 1-2. 위의 작업을 반복하여 내림차순으로 정렬
# i = 0
# ans_arr = []
#
# while i+1 < len(arr):
#     if arr[i] > arr[i+1]:
#         arr[i], arr[i+1] = arr[i+1], arr[i]
#         i += 1
#     else:
#         i += 1
#     if arr[-1] == max(arr):
#         ans_arr += [arr[-1]]
#         arr = arr[:-1]
#         i = 0
#     if len(arr) == 1:
#         ans_arr += arr
#         break
#
#
# print(ans_arr)

# 1-3. 배운 코드
# for j in range(len(arr), 0, -1):
#     for i in range(j-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
# print(arr)

# 한번 더
# N = len(arr)
# for i in range(N, 0, -1):
#     for j in range(i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# 2. 부분집합 생성
# arr = [1, 2, 3, 4]
# sub_set = [[]]

# 로직은 다음과 같다
# 1. [[]]
# 2. [[], [첫번째 값]]
# 3. [[], [첫번째 값], [두번째 값], [첫번째 값, 두번째 값]]
# 위와 같은 방식으로 앞 단계의 부분집합 목록에 arr의 요소들을 하나씩 추가한 것을 추가해주면 됨

# len(sub_set)에 대하여 arr의 값을 이전 단계의 sub_set에 추가한 리스트를 다시 sub_set에 더해준다
# for i in arr:
#     for k in range(len(sub_set)):
#         sub_set.append(sub_set[k] + [i])
#
# print(sub_set)

# 3. 이진탐색
# 이진탐색을 위해선 리스트가 정렬된 상태여야 한다
# 자료의 중앙에 있는 값을 구함
# 그 중앙의 값과 찾아야 하는 값을 비교하여 다음 리스트의 범위를 설정한다
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# find = 7
# cnt = 0
# while len(arr) > 1:
#     if find == arr[len(arr)//2]:
#         cnt += 1
#         break
#     elif find > arr[len(arr)//2]:
#         cnt += 1
#         arr = arr[len(arr)//2 + 1:]
#     elif find < arr[len(arr)//2]:
#         cnt += 1
#         arr = arr[:len(arr)//2]
# print(cnt)

# 4. 선택정렬
# 선택정렬이란 미정렬된 리스트에서 최솟값을 찾는다 -> 최솟값을 가장 앞으로 당긴 후 다음 인덱스부터 쭉 확인해 최솟값을 찾는다 -> 반복
# arr = [4, 2, 6, 4, 5, 2, 4, 6, 7, 8, 2]
# sorted_arr = []
# N = len(arr)
#
# while len(arr) > 0:
#     sorted_arr += [min(arr)]
#     arr.remove(min(arr))
#
# print(sorted_arr)

# 5. 정렬을 함수로 표현해보자
# def array(arr):
#     sorted_arr = []
#     arr2 = arr[:]
#     while len(arr2) > 0:
#         sorted_arr += [min(arr2)]
#         arr2.remove(min(arr2))
#     return sorted_arr
#
# arr = [1, 5, 4, 3, 2, 7, 6, 5, 9, 10]
# a = array(arr)
# print(arr)
# print(a)

# 6. 자주 쓰는 메소드 써보기
# 6-1. append()
arr = [3, 5, 2, 1, 7]
arr.append(2) # arr의 끝부분에 항목 2 추가
arr.append([1, 5]) # arr의 끝부분에 항목 [1, 5] 추가
# print(arr)

# 6-2. index()
# print(arr.index(1)) # arr에서 1의 값을 찾아 해당 인덱스를 반환
# print(arr.index(2)) # arr안에 들어있는 2가 2개인 상황. 이럴땐 가장 처음 만나는 값의 인덱스를 반환(왼쪽)
# print(arr.index(100)) # arr안에 없는 값을 index로 조회하려하면? ValueError가 발생

# 6-3. remove()
arr.remove(3)
# print(arr)
arr2 = [1, 2, 2, 3, 3, 3]
arr2.remove(2) # 제거해줄 값이 여러개 있을 경우 가장 앞에 존재하는 값을 제거(index와 같다고 생각하면 될듯)
# print(arr2)

# 6-4. pop()
arr3 = [1, 4, 2, 7, 6, 4, 8, 9]
print(arr3.pop(4)) # arr3에서 인덱스가 4인 항목을 뽑아낸 후 뽑아낸 항목 반환
print(arr3) # 해당 항목(6)이 뽑아내진 arr3을 출력
print(arr3.pop(99)) # 인덱스 범위를 벗어났으므로 인덱스 에러 발생
print(arr3)