import numpy as np

# 행렬 정의
matrix = np.array([
    [3, 7, 4, 6, 7],
    [2, -3, 5, -7, 0],
    [-2, 3, -3, 4, 2],
    [10, 5, 6, 7, 3],
    [3, 2, 1, 5, 4]
], dtype=float)

# 중간 과정을 출력하며 행렬식 계산
def determinant_with_steps(matrix):
    n = len(matrix)
    det = 1
    steps = []

    for i in range(n):
        # 대각선 요소가 0이면 행 교환
        if matrix[i][i] == 0:
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    det *= -1  # 행 교환 시 행렬식 부호 변경
                    steps.append(f"행 {i+1}와 행 {j+1} 교환:\n{matrix}\n")
                    break
            else:
                steps.append("특이 행렬입니다. 행렬식 = 0\n")
                return 0, steps

        # 현재 행의 대각선 요소를 기준으로 가우스 소거법 적용
        for j in range(i+1, n):
            if matrix[j][i] != 0:
                factor = matrix[j][i] / matrix[i][i]
                matrix[j, i:] -= factor * matrix[i, i:]
                steps.append(f"행 {j+1} -> 행 {j+1} - ({factor:.2f}) * 행 {i+1}:\n{matrix}\n")

    # 대각 성분의 곱
    for i in range(n):
        det *= matrix[i][i]

    return det, steps

# 함수 호출
det_result, steps_output = determinant_with_steps(matrix)

# 중간 과정 출력
for step in steps_output:
    print(step)

# 최종 행렬식 출력
print(f"최종 행렬식: {det_result}")
