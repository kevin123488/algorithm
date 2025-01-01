def solution(triangle):
    answer = 0
    for i in range(len(triangle)):
        if i != 0:
            for k in range(len(triangle[i])):
                if 0 < k < len(triangle[i]) - 1:
                    triangle[i][k] = max(triangle[i - 1][k - 1], triangle[i - 1][k]) + triangle[i][k]
                elif k == 0:
                    triangle[i][k] = triangle[i - 1][k] + triangle[i][k]
                elif k == len(triangle[i]) - 1:
                    triangle[i][k] = triangle[i - 1][k - 1] + triangle[i][k]
                    
    answer = max(triangle[len(triangle) - 1])
    
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))