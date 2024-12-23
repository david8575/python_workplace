import os
import numpy as np

current_dir = os.path.dirname(os.path.abspath(__file__))

input_file_path = os.path.join(current_dir, 'input.txt')
with open(input_file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

matrices = []
matrix = []
matrix_name = ""
row_count = 0

# 입력 파일 파싱
for line in lines:
    line = line.strip()
    if not line:
        continue

    if line.startswith("Matrix 수"):
        # Matrix 수는 무시, 필요한 경우 활용 가능
        continue
    
    if line.startswith("Matrix 정보"):
        # Matrix 정보 시작 무시
        continue

    if line[0].isalpha():
        # 행렬 이름과 크기 정보 파싱
        if matrix:
            matrices.append((matrix_name, np.array(matrix)))
            matrix = []
        parts = line.split()
        matrix_name = parts[0]
        row_count = int(parts[1])  # 행 개수
        continue

    # 행렬 데이터 파싱
    row = list(map(int, line.split()))
    if len(row) > 0:
        matrix.append(row)
        if len(matrix) == row_count:
            matrices.append((matrix_name, np.array(matrix)))
            matrix = []

if matrix:
    matrices.append((matrix_name, np.array(matrix)))

# 행렬식 계산 함수
def calculate_determinant(matrix, name):
    output_file_path = os.path.join(current_dir, 'output.txt')
    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        output_file.write(f"=== 행렬 {name} ===\n")
        output_file.write("행렬:\n")
        output_file.write(str(matrix) + "\n\n")
        
        def cofactor_expansion(matrix, row=0, depth=0, all_steps=None, step_values=None, detailed_steps=None):
            if all_steps is None:
                all_steps = {}
            if step_values is None:
                step_values = []
            if detailed_steps is None:
                detailed_steps = []

            if matrix.shape[0] == 2:
                result = np.linalg.det(matrix)
                detailed_steps.append(f"|{matrix[0][0]} {matrix[0][1]}|\n|{matrix[1][0]} {matrix[1][1]}| = {result}")
                return result, all_steps, step_values, detailed_steps
            
            cofactor_sum = 0
            if depth not in all_steps:
                all_steps[depth] = []
            all_steps[depth].append(f"Det(\n{matrix}\n)=\n")
            
            for col in range(matrix.shape[1]):
                minor_matrix = np.delete(matrix, row, axis=0)
                minor_matrix = np.delete(minor_matrix, col, axis=1)
                cofactor = ((-1)**(row + col)) * matrix[row, col]
                
                all_steps[depth].append(f"{'+' if cofactor > 0 else ''}{cofactor} * Det(\n{minor_matrix}\n)\n\n")
                
                minor_determinant, all_steps, step_values, detailed_steps = cofactor_expansion(
                    minor_matrix, depth=depth+1, all_steps=all_steps, step_values=step_values, detailed_steps=detailed_steps
                )
                term_value = cofactor * minor_determinant
                cofactor_sum += term_value
                if depth == 0:
                    step_values.append(term_value)
            
            return cofactor_sum, all_steps, step_values, detailed_steps
        
        det_cofactor, all_steps, step_values, detailed_steps = cofactor_expansion(matrix)
        output_file.write("1. 코팩터 전개 방식:\n")
        for depth in sorted(all_steps.keys()):
            output_file.write(f"--- Depth {depth} ---\n")
            output_file.write("".join(all_steps[depth]))
            output_file.write("\n")
        
        output_file.write("\n".join(detailed_steps) + "\n\n")
        
        if step_values:
            step_sum = " + ".join(f"({val})" for val in step_values)
            output_file.write(f"코팩터 전개 방식 행렬식 계산: {step_sum} = {det_cofactor}\n\n")
        else:
            output_file.write(f"코팩터 전개 방식 행렬식: {det_cofactor}\n\n")
        
        def determinant_with_steps(matrix):
            n = len(matrix)
            det = 1
            steps = []

            for i in range(n):
                if matrix[i][i] == 0:
                    for j in range(i+1, n):
                        if matrix[j][i] != 0:
                            matrix[[i, j]] = matrix[[j, i]]
                            det *= -1
                            steps.append(f"행 {i+1}와 행 {j+1} 교환:\n{matrix}\n")
                            break
                    else:
                        steps.append("특이 행렬입니다. 행렬식 = 0\n")
                        return 0, steps

                for j in range(i+1, n):
                    if matrix[j][i] != 0:
                        factor = matrix[j][i] / matrix[i][i]
                        matrix[j, i:] -= factor * matrix[i, i:]
                        steps.append(f"행 {j+1} -> 행 {j+1} - ({factor:.2f}) * 행 {i+1}:\n{matrix}\n")

            for i in range(n):
                det *= matrix[i][i]

            return det, steps

        matrix_copy = matrix.astype(float).copy()
        det_gauss, steps_output = determinant_with_steps(matrix_copy)

        output_file.write("2. 가우스 소거법 방식:\n")
        for step in steps_output:
            output_file.write(step + "\n")
        
        output_file.write(f"가우스 소거법 방식 행렬식: {det_gauss}\n\n")
        output_file.write("=" * 50 + "\n\n")

# 기존 output.txt 초기화
open(os.path.join(current_dir, 'output.txt'), 'w').close()

# 각 행렬에 대해 calculate_determinant 호출
for name, matrix in matrices:
    print(f"Calculating determinant for matrix {name}")
    calculate_determinant(matrix, name)
