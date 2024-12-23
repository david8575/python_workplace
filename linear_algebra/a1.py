# 학과 / 학번 / 이름 / 역할
# 인공지능학과 / 21012037 / 이수찬 / 파일입출력 코드 작성
# 소프트웨어학과 / 21011772 / 이성훈 / Matrix trace 연산 코드 작성
# 소프트웨어학과 / 20003322 / 박세훈 / Matrix + 연산 코드 작성
# 인공지능학과 / 23012137 / 이혜정 / Matrix * 연산 코드 작성

import math as m
import os

# 파일 입력 받는 함수: parse_file
def parse_file(file_path):
    # 파일에서 입력 받은 행렬과 연산 정보를 저장
    matrices = {}
    operations = []
    
    # lines에 파일에서 읽어 온 정보를 한 줄씩 저장
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # 파일의 첫줄을 행렬의 수
    num_matrices = int(lines[0].strip())  
    index = 1

    # 행렬의 수만큼 행렬 정보 입력받기
    for _ in range(num_matrices):
        matrix_name = lines[index].strip().split()[0]
        rows, cols = map(int, lines[index].strip().split()[1:])
        matrix_data = []
        
        for i in range(1, rows + 1):
            matrix_data.append(list(map(int, lines[index + i].strip().split())))
        
        matrices[matrix_name] = matrix_data
        index += rows + 1

    # 행렬 정보를 읽은 후 다음 줄부터 연산 정보 입력받기
    num_operations = int(lines[index].strip())
    index += 1

    # 연산 수만큼 연산 정보 입력받기
    for i in range(num_operations):
        operations.append(lines[index].strip())
        index += 1

    # 파싱 결과 반환
    return matrices, operations

# 두 행렬을 더하는 함수: add_matrix
def add_matrix(m1, m2):
    # 각 행렬의 행과 열을 저장
    m1_row, m1_col = len(m1), len(m1[0])
    m2_row, m2_col = len(m2), len(m2[0])

    # 연산이 가능한 경우
    if m1_row == m2_row and m1_col == m2_col:
        m3 = []
        for i in range(m1_row):
            row = []
            for j in range(m1_col):
                row.append(m1[i][j] + m2[i][j])
            m3.append(row)
        return m3
    # 불가능한 경우
    else:
        print("Invalid calculation")
        return None

# 두 행렬을 곱하는 함수: mul_matrix
def mul_matrix(m1, m2):
    # 각 행렬의 행과 열을 저장
    m1_row, m1_col = len(m1), len(m1[0])
    m2_row, m2_col = len(m2), len(m2[0])

    # 연산이 가능한 경우
    if m1_col == m2_row:
        m3 = [[0 for _ in range(m2_col)] for _ in range(m1_row)]
        for i in range(m1_row):
            for j in range(m2_col):
                for k in range(m1_col):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3 
    # 연산이 불가능한 경우
    else:
        print("Invalid calculation")
        return None

# 행렬의 trace를 구하는 함수: trace_matrix
def trace_matrix(m):
    # 행렬의 행과 열을 저장
    row, col = len(m), len(m[0])
    
    # 연산이 가능한 경우
    if row == col:
        trace = 0
        for i in range(row):
            trace += m[i][i]
        return trace
    # 연산이 불가능한 경우
    else:
        print("Invalid calculation")
        return None

# 행렬의 연산을 수행한 후 파일에 저장하는 함수
def output(file_path, matrices, operations):
    # output.txt에 쓰기
    with open(file_path, 'w') as f:
        # 연산을 하나씩 수행
        for operation in operations:
            parts = operation.split()
            op_type = parts[0]
            
            if parts[1].isdigit():
                parts.pop(1)  
            
            # 더하기 연산의 경우 
            if op_type == 'Add':
                # 행렬의 정보를 불러오기
                m1_name = parts[1]
                m2_name = parts[2]
                m1 = matrices[m1_name]
                m2 = matrices[m2_name]
                
                # 결과 생성
                result = add_matrix(m1, m2)
                
                # 유효한 연산이였던 경우
                if result:
                    # output.txt에 형식에 맞게 작성
                    f.write(f"{op_type} {m1_name} {m2_name}\n")
                    for row in result:
                        f.write(" ".join(map(str, row)) + "\n")
            
            # 곱하기 연산의 경우 
            elif op_type == 'Mul':
                # 행렬의 정보를 불러오기
                m1_name = parts[1]
                m2_name = parts[2]
                m1 = matrices[m1_name]
                m2 = matrices[m2_name]
                
                # 결과 생성
                result = mul_matrix(m1, m2)
                
                # 유효한 연산이였던 경우
                if result:
                    # output.txt에 형식에 맞게 작성
                    f.write(f"{op_type} {m1_name} {m2_name}\n")
                    for row in result:
                        f.write(" ".join(map(str, row)) + "\n")
                        
            # trace 연산의 경우 
            elif op_type == 'Trace':
                # 행렬의 정보를 불러오기
                m_name = parts[1]
                m = matrices[m_name]
                
                # 결과 생성
                result = trace_matrix(m)
                # 유효한 연산이였던 경우
                if result :
                    # output.txt에 형식에 맞게 작성
                    f.write(f"{op_type} {m_name}\n{result}\n")


# 입출력 파일 정보 저장
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_dir, 'input.txt')
output_file_path = os.path.join(current_dir, 'output.txt')

# input.txt에서 행렬과 연산정보 저장
matrices, operations = parse_file(input_file_path)

# 결과 저장
output(output_file_path, matrices, operations)