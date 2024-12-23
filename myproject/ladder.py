import random

def draw_ladder(width, height):
    ladder = []
    for _ in range(height):
        row = ['|'] * width
        ladder.append(row)
    return ladder

def print_ladder(ladder):
    for row in ladder:
        print('  '.join(row))
    print()

def move(ladder, row, col):
    if col > 0 and ladder[row][col - 1] == '-':
        col -= 2
    elif col < len(ladder[row]) - 1 and ladder[row][col + 1] == '-':
        col += 2
    row += 1
    return row, col

def ladder_game(width, height):
    ladder = draw_ladder(width, height)
    for row in range(height):
        for col in range(1, width, 2):
            if random.randint(0, 1):
                ladder[row][col] = '-'
    print("사다리를 그렸습니다:")
    print_ladder(ladder)
    
    player_col = int(input("시작할 열을 선택하세요 (1부터 {}까지): ".format(width)))
    player_row = 0
    
    while player_row < height:
        player_row, player_col = move(ladder, player_row, player_col)
        print_ladder(ladder)
        if player_row < height:
            move_direction = input("다음으로 가시겠습니까? (오른쪽/왼쪽/아래): ").lower()
            if move_direction == "오른쪽":
                player_col += 2
            elif move_direction == "왼쪽":
                player_col -= 2
    
    print("도착했습니다!")

# 게임 시작
width = 10  # 사다리의 열 개수
height = 5  # 사다리의 행 개수
ladder_game(width, height)