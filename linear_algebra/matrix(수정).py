# 학과 / 학번 / 이름 / 역할
# 인공지능학과 / 21012037 / 이수찬 / 파일입력 코드 작성
# 소프트웨어학과 / 21011772 / 이성훈 / Matrix trace 연산 코드 작성
# 소프트웨어학과 / 20003322 / 박세훈 / Matrix + 연산 코드 작성
# 인공지능학과 / 23012137 / 이혜정 / Matrix * 연산 코드 작성
# 인공지능학과 / 23012125 / 유은재 / 파일출력 코드 작성

import math  # math 모듈을 불러옴 (필요시 사용 가능)
import os
# 파일 읽기
current_dir = os.path.dirname(os.path.abspath(__file__))

input_file_path = os.path.join(current_dir, 'input.txt')
with open(input_file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 입력 파일을 읽어서 각 줄을 리스트로 저장

# 결과를 출력할 파일 경로
output_file_path = os.path.join(current_dir, 'output.txt')  # 출력 파일 경로 설정
with open(output_file_path, 'w', encoding='utf-8') as output_file:  # 출력 파일을 쓰기 모드로 열기

    # 행렬 개수 읽기
    matrix_count = int(lines[0].split()[2])  # 입력 파일의 첫 번째 줄에서 'Matrix 수' 부분을 파싱하여 행렬 개수를 저장

    # 행렬 저장 딕셔너리
    matrices = {}  # 각 행렬을 저장할 딕셔너리 생성
    line_idx = 2  # 'Matrix 정보:' 이후부터 시작할 줄 인덱스 (세 번째 줄)

# 행렬 정보 파싱
    for _ in range(matrix_count):  # matrix_count만큼 반복 (각 행렬에 대해 수행)
        matrix_info = lines[line_idx].strip().split()  # 행렬 이름과 행/열 정보를 추출 (예: 'A 3 3')
        matrix_name = matrix_info[0]  # 행렬 이름 저장 (예: 'A')
        rows, cols = int(matrix_info[1]), int(matrix_info[2])  # 행렬의 행 수와 열 수를 정수로 변환하여 저장
        
        # 행렬 데이터 파싱
        matrix_data = []  # 행렬 데이터를 저장할 리스트 생성
        for i in range(rows):  # 행 수만큼 반복
            line_idx += 1  # 줄 인덱스 이동
            matrix_data.append(list(map(int, lines[line_idx].strip().split())))  # 각 행 데이터를 읽고 정수 리스트로 변환하여 저장

        matrices[matrix_name] = matrix_data  # 딕셔너리에 행렬 이름을 키로, 데이터를 값으로 저장

        line_idx += 2  # 다음 행렬 정보를 읽기 위해 줄 인덱스 증가

    # 연산 개수 읽기
    operation_count = int(lines[line_idx].strip().split()[2])  # '연산 수'를 파싱하여 연산 개수를 정수로 저장
    line_idx += 2  # '연산 정보:' 다음 줄로 이동

    # 두 행렬을 더하는 함수 정의
    def matrix_add(matrix1, matrix2):
        # 각 행과 열에서 두 행렬의 대응되는 원소를 더한 결과 행렬 반환
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    # 두 행렬을 곱하는 함수 정의
    def matrix_mul(matrix1, matrix2):
        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]  # 결과 행렬을 0으로 초기화
        for i in range(len(matrix1)):  # 첫 번째 행렬의 각 행에 대해
            for j in range(len(matrix2[0])):  # 두 번째 행렬의 각 열에 대해
                for k in range(len(matrix1[0])):  # 첫 번째 행렬의 열과 두 번째 행렬의 행을 곱함
                    result[i][j] += matrix1[i][k] * matrix2[k][j]  # 곱한 값을 결과 행렬에 더함
        return result  # 결과 행렬 반환

    # 행렬의 대각합(Trace)을 계산하는 함수 정의
    def matrix_trace(matrix):
        return sum(matrix[i][i] for i in range(len(matrix)))  # 대각선 원소들의 합을 반환

    # 연산 수행
    for _ in range(operation_count):  # 연산 개수만큼 반복
        operation_info = lines[line_idx].strip().split()  # 연산 정보를 파싱
        operation = operation_info[0]  # 연산 종류 ('Add', 'Mul', 'Trace') 저장

        if operation == 'Add':  # 덧셈 연산일 경우
            factor = int(operation_info[1]) -1 # 연산에 필요한 매개변수 (이 코드에서는 사용 안 함)
            result = None
            valid_operation = True

            for i in range (factor):
                if i == 0:
                    matrix1 = matrices[operation_info[2]]  # 첫 번째 행렬 이름으로 행렬 데이터 불러옴
                else:
                    matrix1 = result

                matrix2 = matrices[operation_info[i + 3]]  # 두 번째 행렬 이름으로 행렬 데이터 불러옴
                
                matrix1_row = len(matrix1)
                matrix1_column = len(matrix1[0])
                matrix2_row = len(matrix2)
                matrix2_column = len(matrix2[0])

                if(matrix1_row != matrix2_row or matrix1_column != matrix2_column):
                    output_file.write("잘못된 연산입니다\n")
                    valid_operation = False
                    break

                result = matrix_add(matrix1, matrix2)  # 두 행렬을 더함

            if valid_operation:
                output_file.write("Add")  # 연산 결과 출력
                for i in range (2, int(operation_info[1]) + 2):
                    output_file.write(f" {operation_info[i]}")

                output_file.write("\n")

                for row in result:  # 결과 행렬 각 행을 출력
                    output_file.write(' '.join(map(str, row)) + '\n')  # 각 행을 파일에 저장

        elif operation == 'Mul':  # 곱셈 연산일 경우
            factor = int(operation_info[1]) - 1 # 연산에 필요한 매개변수 (이 코드에서는 사용 안 함)
            result = None
            valid_operation = True

            for i in range (factor):
                if i == 0:
                    matrix1 = matrices[operation_info[2]]  # 첫 번째 행렬 이름으로 행렬 데이터 불러옴
                else:
                    matrix1 = result
                matrix2 = matrices[operation_info[i + 3]]  # 두 번째 행렬 불러옴

                matrix1_row = len(matrix1)
                matrix1_column = len(matrix1[0])
                matrix2_row = len(matrix2)
                matrix2_column = len(matrix2[0])

                if(matrix1_column != matrix2_row):
                    output_file.write("잘못된 연산입니다\n")
                    valid_operation = False
                    break

                result = matrix_mul(matrix1, matrix2)  # 두 행렬을 곱함

            if valid_operation:
                output_file.write("Mul")  # 연산 결과 출력
                for i in range (2, int(operation_info[1]) + 2):
                    output_file.write(f" {operation_info[i]}")

                output_file.write("\n")

                for row in result:  # 결과 행렬 각 행을 출력
                    output_file.write(' '.join(map(str, row)) + '\n')  # 각 행을 파일에 저장

        elif operation == 'Trace':  # 대각합 연산일 경우
            matrix = matrices[operation_info[1]]  # 대각합을 구할 행렬을 불러옴
            valid_operation = True

            matrix_row = len(matrix)
            matrix_column = len(matrix[0])

            if (matrix_row != matrix_column):
                    output_file.write("잘못된 연산입니다\n")
                    valid_operation = False
                 

            if valid_operation:
                result = matrix_trace(matrix)# 대각합 계산
                output_file.write(f"Trace {operation_info[1]}\n{result}\n")  # 연산 결과 출력

        # 연산 후 다음 줄로 이동 (line_idx 증가)
        line_idx += 1  # 다음 연산 정보를 읽기 위해 줄 인덱스 증가