# N * N짜리 2차원 리스트를 받는다

arr = [[1, 2, 3, 2, 1],
       [2, 2, 3, 1, 3],
       [1, 2, 1, 1, 3],
       [2, 2, 1, 1, 1],
       [1, 1, 1, 1, 1]]

# 1. arr의 각 요소에 대해 해당 요소를 중심으로 한 3*3 사각형의 넓이만큼의 합을 구하고(만약 원래 범위를 벗어날 경우 해당 사각형은 무효처리)
# 그 합들의 합을 구한다.
# 2. arr의 각 요소에 대해