from fractions import Fraction

def row_operation(list1, list2, k):
    list3 = []
    for i in range(len(list1)):
        # Fraction을 사용하여 연산 후 결과를 분수 형태로 저장
        a = Fraction(list1[i]) * Fraction(k) + Fraction(list2[i])
        list3.append(a)
    return list3

def augment_identity(matrix, n):
    # Augment 행렬: 주어진 행렬의 우측에 단위 행렬 추가
    for i in range(n):
        matrix[i] += [Fraction(1) if i == j else Fraction(0) for j in range(n)]
    return matrix

def inverse(matrix, n):
    matrix = augment_identity(matrix, n)
    
    
    
    while True:
        # 현재 행렬 상태 출력
        for i in range(n):
            for j in range(2 * n):
                print(matrix[i][j], end=" ")
            print()
        
        print('1번: 행 바꾸기, 2번: 행에 곱하기, 3번 행에 곱하고 더하고 대체, 4번: 종료>> ', end="")
        oper = int(input())
        
        if oper == 1:
            print('바꿀 행 2개 입력>> ', end="")
            a, b = map(int, input().split())
            matrix[a-1], matrix[b-1] = matrix[b-1], matrix[a-1]
            print(f'R{a} <-> R{b}')
        elif oper == 2:
            print("곱할 행>> ", end="")
            r = int(input())
            s = Fraction(input("곱할 값 입력>> "))
            for i in range(2 * n):
                matrix[r-1][i] *= s
            print(f'R{r} X ({s}) -> R{r}')
        elif oper == 3:
            print("연산할 행 두 개 입력>> ", end="")
            a, b = map(int, input().split())
            s = Fraction(input("곱할 값 입력>> "))
            matrix[b-1] = row_operation(matrix[a-1], matrix[b-1], s)
            print(f'R{a} X ({s}) + R{b} -> R{b}')
        elif oper == 4:
            # Augmented 행렬 출력 (좌측은 원래 행렬, 우측은 단위 행렬 변환 중간 결과)
            for i in range(n):
                for j in range(2 * n):
                    print(matrix[i][j], end=" ")
                print()
            return
        
        

# 예제 행렬 초기화
matrix = [
    [2, 1, 3, 4, 5],
    [1, 2, 4, 3, 1],
    [3, 4, 2, 1, 5],
    [4, 3, 1, 2, 3],
    [5, 1, 5, 3, 2],
]
inverse(matrix, 5)