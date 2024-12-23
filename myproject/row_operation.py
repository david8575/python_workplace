import numpy as np

def row_operation_steps(matrix):
    m, n = matrix.shape
    steps = []
    matrix = matrix.astype(float)  # 실수로 변환하여 연산

    # 상삼각 행렬을 만들기 위한 과정
    for i in range(min(m, n)):
        # 피봇을 1로 만드는 과정
        if matrix[i, i] != 0:
            matrix[i] = matrix[i] / matrix[i, i]
            steps.append(f"R{i+1} / {matrix[i, i]}")
        
        # 아래 행을 0으로 만드는 과정
        for j in range(i+1, m):
            if matrix[j, i] != 0:
                factor = matrix[j, i]
                matrix[j] = matrix[j] - factor * matrix[i]
                steps.append(f"R{j+1} - ({factor})*R{i+1}")
                
        # 각 단계마다 행렬 출력
        steps.append(matrix.copy())
    
    # 상삼각 행렬에서 역방향으로 0을 만들기
    for i in range(min(m, n)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if matrix[j, i] != 0:
                factor = matrix[j, i]
                matrix[j] = matrix[j] - factor * matrix[i]
                steps.append(f"R{j+1} - ({factor})*R{i+1}")
                
        # 각 단계마다 행렬 출력
        steps.append(matrix.copy())

    return steps

# 테스트 행렬
matrix = np.array([[2, 1, -1, -3],
                   [1, 3, 2, 1],
                   [3, 1, 3, 4]], dtype=float)

steps = row_operation_steps(matrix)

# 각 과정을 출력
for step in steps:
    print(step)
