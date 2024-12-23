def paint_chess(board, m, n):
    pattern1 = [list("WBWBWBWB"), list("BWBWBWBW")] * 4
    pattern2 = [list("BWBWBWBW"), list("WBWBWBWB")] * 4
    min_value = 1000000

    for first_row in range(m-7):
        for first_col in range(n-7):
            count1 = 0
            count2 = 0 
            for i in range(8):
                for j in range(8):
                    if board[first_row+i][first_col+j] != pattern1[i][j]:
                        count1 += 1
                    if board[first_row+i][first_col+j] != pattern2[i][j]:
                        count2 += 1
            min_value = min(min_value, count1, count2)
        
    return min_value

m, n = map(int, input().split())
board = []*n
for i in range(m):
    str = input()
    board[i] = str

print(paint_chess(board, m, n))